#!/usr/bin/env python3
"""Finite checks for Lattice Hidden Metrology. These do not test hardness.

Run from any directory. Use --write to replace the stored report after a
successful run. Numerical tolerances and tested parameters are reported.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eigh
from numpy.polynomial.hermite import hermgauss

PI = math.pi
RNG = np.random.default_rng(20261023)
CHECKS = 0

def require(ok: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not bool(ok):
        raise AssertionError(message)

def parameters(beta: float, gamma: float, R: float) -> dict[str, float]:
    if min(beta, gamma, R) <= 0:
        raise ValueError('beta, gamma and R must be positive')
    S2 = gamma * gamma + beta * beta
    a = gamma / S2
    b2 = beta * beta / S2
    s2 = PI / (R * R)
    c2, h2 = b2 + s2, 1 + s2
    return dict(S2=S2, a=a, b2=b2, c2=c2, h2=h2,
                r2=c2 / (a*a), zeta2=beta*beta+PI*gamma*gamma/(PI+R*R))

def discrete_gaussian(S2: float):
    # exp(-pi*k^2/S2) beyond this cutoff is far below double precision.
    cutoff = int(math.ceil(math.sqrt(40*S2/PI))) + 2
    k = np.arange(-cutoff, cutoff+1, dtype=float)
    p = np.exp(-PI*k*k/S2)
    return k, p / p.sum()

def gaussian_pdf(t, width2: float):
    return np.exp(-PI*np.asarray(t)**2/width2)/math.sqrt(width2)

def mixture_pdf_and_derivative(t, p: dict[str, float]):
    k, weights = discrete_gaussian(p['S2'])
    d = np.asarray(t)[..., None] - p['a']*k
    f = np.exp(-PI*d*d/p['c2'])/math.sqrt(p['c2'])
    return f@weights, (-2*PI*d*f/p['c2'])@weights

def characteristic(t: float, p: dict[str, float]) -> float:
    k, weights = discrete_gaussian(p['S2'])
    return float(np.exp(-PI*(p['c2']*t*t+p['h2']*(1-t*t))/p['a']**2)
                 * (np.cos(2*PI*k*t)@weights))

def coherent_vectors(qmeans: np.ndarray, cutoff: int) -> np.ndarray:
    alpha = qmeans / math.sqrt(2)
    out = np.empty((len(alpha), cutoff), dtype=float)
    out[:, 0] = np.exp(-alpha*alpha/2)
    for j in range(1, cutoff):
        out[:, j] = out[:, j-1]*alpha/math.sqrt(j)
    return out

def density_from_mixture(beta: float, gamma: float, R: float,
                         cutoff: int = 40, nodes: int = 80):
    p = parameters(beta, gamma, R)
    k, weights = discrete_gaussian(p['S2'])
    z, gh = hermgauss(nodes)
    gh = gh / math.sqrt(PI)
    t = (p['a']*k[:,None] + math.sqrt(p['b2']/PI)*z[None,:]).ravel()
    wt = (weights[:,None]*gh[None,:]).ravel()
    v = coherent_vectors(R*t, cutoff)
    sigma = v.T@(wt[:,None]*v)
    v0 = coherent_vectors(R*z/math.sqrt(PI), cutoff)
    tau = v0.T@(gh[:,None]*v0)
    return sigma, tau

def fisher_numeric(p: dict[str, float]) -> float:
    def integrand(t):
        f, fp = mixture_pdf_and_derivative(t, p)
        if f < 1e-290:
            return 0.0
        score = fp/f + 2*PI*t/p['h2']
        return float(f*score*score*p['h2']/(2*PI))
    k, weights = discrete_gaussian(p['S2'])
    bound = abs(p['a']*k[-1]) + 7*math.sqrt(p['c2'])
    # Integrate each mixture spacing to resolve narrow peaks reliably.
    breaks = np.linspace(-bound,bound, max(100,int(4*bound/p['a']))+1)
    return sum(quad(integrand,l,r,epsabs=2e-10,epsrel=2e-10)[0]
               for l,r in zip(breaks[:-1],breaks[1:]))

def qfi_two_mode(sigma: np.ndarray, tau: np.ndarray) -> float:
    # G=Q1 P2-P1 Q2. Product eigensystems avoid diagonalizing a K^2 matrix.
    d = len(sigma)
    annihilation = np.diag(np.sqrt(np.arange(1,d)),1)
    Q = (annihilation + annihilation.T)/math.sqrt(2)
    P = (annihilation - annihilation.T)/(1j*math.sqrt(2))
    ps, us = eigh(sigma)
    pt, ut = eigh(tau)
    ps, pt = np.maximum(ps,0),np.maximum(pt,0)
    eigenvalues = np.outer(ps,pt).ravel()
    G = np.kron(us.T@Q@us,ut.T@P@ut)-np.kron(us.T@P@us,ut.T@Q@ut)
    denom = eigenvalues[:,None]+eigenvalues[None,:]
    diff = eigenvalues[:,None]-eigenvalues[None,:]
    factor = np.divide(2*diff*diff,denom,out=np.zeros_like(denom),where=denom>1e-15)
    return float(np.sum(factor*np.abs(G)**2))

def run():
    report = {'scope':'Finite algebra, quadrature, Fock-cutoff and seeded estimator checks; not cryptographic or asymptotic proof.',
              'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
              'seed':20261023}
    # 1. Mixture/Fourier normalization and exact population gap.
    max_density_error = max_gap_violation = max_variance_error = 0.0
    cases = [(b,g,r) for b in [.15,.4,.8] for g in [1.3,2.5,4.] for r in [1.,3.,8.]]
    gap_count=0
    for beta,gamma,R in cases:
        p=parameters(beta,gamma,R)
        k,wt=discrete_gaussian(p['S2'])
        ell=np.arange(-50,51)
        C=float(np.exp(-PI*p['S2']*ell*ell).sum())
        var_mix=float(p['a']**2*(wt@k**2)+p['b2']/(2*PI))
        var_fourier=1/(2*PI)-gamma*gamma/C*float((ell*ell*np.exp(-PI*p['S2']*ell*ell)).sum())
        max_variance_error=max(max_variance_error,abs(var_mix-var_fourier))
        require(abs(var_mix-var_fourier)<1e-12,'moment identity')
        require(var_mix<=1/(2*PI)+1e-13,'moment upper bound')
        for t in np.linspace(-1.7,1.7,13):
            mixture=float(gaussian_pdf(t-p['a']*k,p['b2'])@wt)
            fourier=math.exp(-PI*t*t)/C*float((np.exp(-PI*beta*beta*ell*ell)*np.cos(2*PI*gamma*ell*t)).sum())
            max_density_error=max(max_density_error,abs(mixture-fourier))
            require(abs(mixture-fourier)<2e-11,'mixture/Fourier density')
        A=math.exp(-PI*p['r2'])
        for t in np.linspace(-1.,1.,101):
            upper=A*math.exp(-PI*p['S2']*(1-t*t))
            gap=characteristic(float(t),p)-upper
            max_gap_violation=max(max_gap_violation,gap)
            require(gap<2e-13,'population characteristic gap')
            gap_count+=1
    report['density_and_gap']={'parameter_cases':len(cases),'direction_checks':gap_count,
         'max_density_error':max_density_error,'max_variance_error':max_variance_error,
         'max_gap_violation':max_gap_violation}
    # 2. Direct Gaussian integral verifies the non-Hermitian Fourier operator kernel.
    kernel_error=0.0
    for R in [.6,1.8,4.]:
        for gamma in [1.2,2.4]:
            for ell in [1,2]:
                q,qp=RNG.normal(size=2)
                def integrand(x):
                    return math.exp(-PI*x*x-((q-R*x)**2+(qp-R*x)**2)/2)/math.sqrt(PI)
                real=quad(lambda x:integrand(x)*math.cos(2*PI*gamma*ell*x),-8,8,epsabs=1e-12)[0]
                imag=quad(lambda x:integrand(x)*math.sin(2*PI*gamma*ell*x),-8,8,epsabs=1e-12)[0]
                tau=math.exp(-(q*q+qp*qp)/2+R*R*(q+qp)**2/(4*(PI+R*R)))/math.sqrt(PI+R*R)
                predicted=tau*np.exp(-PI*PI*gamma*gamma*ell*ell/(PI+R*R)+1j*PI*gamma*ell*R*(q+qp)/(PI+R*R))
                err=abs(real+1j*imag-predicted)
                kernel_error=max(kernel_error,float(err))
                require(err<2e-11,'Fourier optical kernel')
    report['optical_kernel']={'cases':12,'max_absolute_error':kernel_error}
    # 3. Finite Fock trace distance lies within analytical bounds.
    distances=[]
    for beta,gamma,R in [(.3,1.3,.8),(.3,1.3,1.6),(.3,1.3,2.4),(.7,2.,2.4)]:
        p=parameters(beta,gamma,R)
        sigma,tau=density_from_mixture(beta,gamma,R)
        trace_deficit=max(abs(1-np.trace(sigma)),abs(1-np.trace(tau)))
        require(trace_deficit<2e-10,'Fock mass convergence')
        D=.5*float(np.abs(eigh(sigma-tau,eigvals_only=True)).sum())
        ell=np.arange(1,100)
        C=1+2*float(np.exp(-PI*p['S2']*ell*ell).sum())
        upper=float((np.exp(-PI*p['zeta2']*ell*ell).sum()+np.exp(-PI*p['S2']*ell*ell).sum())/C)
        lower=.5*math.exp(-PI*p['r2'])*(-math.expm1(-PI*p['S2']))
        require(lower-2e-9<=D<=upper+2e-9,'trace-distance sandwich')
        distances.append({'beta':beta,'gamma':gamma,'R':R,'distance':D,'lower':lower,'upper':upper,'trace_deficit':float(trace_deficit)})
    report['trace_distance']=distances
    # 4. Mixed-state QFI is checked, not the label-conditioned pure-state QFI.
    fisher=[]
    for beta,gamma,R in [(.25,1.4,1.0),(.25,1.4,1.8),(.6,1.4,1.8)]:
        p=parameters(beta,gamma,R)
        I=fisher_numeric(p)
        bound=2*PI*gamma*gamma/(p['h2']*math.sinh(2*PI*p['r2']))
        qfis=[]
        for cutoff in [28,36]:
            sigma,tau=density_from_mixture(beta,gamma,R,cutoff=cutoff,nodes=96)
            qfis.append(qfi_two_mode(sigma,tau))
        convergence=abs(qfis[1]-qfis[0])
        require(convergence<3e-6,'QFI cutoff convergence')
        require(bound<=I+1e-9,'homodyne FI witness')
        require(I<=qfis[-1]+3e-6,'measurement monotonicity')
        require(qfis[-1]<=2*R*R/PI+3e-6,'mixed-state QFI upper bound')
        fisher.append({'beta':beta,'gamma':gamma,'R':R,'witness_lower':bound,'homodyne_fi':I,'mixed_qfi':qfis[-1],
                       'qfi_upper':2*R*R/PI,'cutoff_difference':convergence})
    report['fisher_information']=fisher
    high_resolution=[]
    for beta,gamma in [(.2,2.),(.1,3.),(.05,4.)]:
        R=gamma/beta
        p=parameters(beta,gamma,R)
        I=fisher_numeric(p)
        lower=2*PI*gamma*gamma/(p['h2']*math.sinh(2*PI*p['r2']))
        require(lower<=I+1e-7,'resolved homodyne witness')
        require(I<=2*R*R/PI+1e-6,'resolved FI quantum upper bound')
        high_resolution.append({'beta':beta,'gamma':gamma,'R':R,'homodyne_fi_over_R2':I/(R*R),
                                'witness_over_R2':lower/(R*R),'limiting_witness':1/(1+PI)})
    report['resolved_fisher']=high_resolution
    # 5. Exact geometry/sign invariance in multiple dimensions.
    geom_error=0.0
    for n in [2,4,10,20]:
        J=np.kron(np.eye(n//2),np.array([[0.,-1.],[1.,0.]]))
        require(np.max(np.abs(J@J+np.eye(n)))<1e-14,'complex structure')
        for _ in range(20):
            w=RNG.normal(size=n);w/=np.linalg.norm(w)
            theta=float(RNG.uniform(-PI/8,PI/8))
            v=math.cos(theta)*w+math.sin(theta)*J@w
            for s1 in [-1,1]:
                for s2 in [-1,1]:
                    u1,u2=s1*w,s2*v
                    est=math.atan(float((J@u1)@u2)/float(u1@u2))
                    geom_error=max(geom_error,abs(est-theta))
                    require(abs(est-theta)<2e-14,'sign-invariant angle')
            for nc,ns in [(1,1),(3,7),(10,2)]:
                I=1.7
                tangent=np.zeros(n-1);tangent[0]=1
                block=np.block([[(nc+ns)*I*np.eye(n-1),ns*I*tangent[:,None]],
                                [ns*I*tangent[None,:],np.array([[ns*I]])]])
                schur=block[-1,-1]-block[-1,:-1]@np.linalg.solve(block[:-1,:-1],block[:-1,-1])
                require(abs(schur-nc*ns/(nc+ns)*I)<1e-12,'nuisance Schur complement')
    report['geometry']={'max_angle_error':geom_error,'dimensions':[2,4,10,20],'sign_cases':320}
    # The null is invariant under real mode mixing, NOT arbitrary optical phase shifts.
    null_errors=[]
    for n in [2,4,10]:
        J=np.kron(np.eye(n//2),np.array([[0.,-1.],[1.,0.]]))
        O=math.cos(.27)*np.eye(n)+math.sin(.27)*J
        S=np.block([[O,np.zeros((n,n))],[np.zeros((n,n)),O]])
        V=np.diag([.5+9/(2*PI)]*n+[.5]*n)
        e=float(np.max(np.abs(S@V@S.T-V)))
        null_errors.append(e)
        require(e<1e-13,'real passive null invariance')
        phase=np.eye(2*n)
        phase[0,0]=phase[n,n]=math.cos(.27)
        phase[0,n]=-math.sin(.27);phase[n,0]=math.sin(.27)
        require(np.max(np.abs(phase@V@phase.T-V))>.1,'generic phase leakage counterexample')
    report['null_symmetry']={'max_real_mixing_covariance_error':max(null_errors),
                            'generic_phase_counterexamples':3}
    # 6. Small seeded demonstrations of the actual two-batch estimator.
    # These use a convenient circle grid, not an empirical test of the asymptotic sample bound.
    beta,gamma,R=.2,3.,15.
    p=parameters(beta,gamma,R);k,wt=discrete_gaussian(p['S2'])
    grid=np.linspace(0,PI,2048,endpoint=False)
    dirs=np.column_stack([np.cos(grid),np.sin(grid)])
    def sample(axis_angle,count):
        T=p['a']*RNG.choice(k,size=count,p=wt)+RNG.normal(scale=math.sqrt(p['c2']/(2*PI)),size=count)
        Z=RNG.normal(scale=math.sqrt(p['h2']/(2*PI)),size=count)
        return np.column_stack([T*math.cos(axis_angle)-Z*math.sin(axis_angle),T*math.sin(axis_angle)+Z*math.cos(axis_angle)])
    def axis(data):
        objective=np.empty(len(dirs))
        for i in range(0,len(dirs),128):
            objective[i:i+128]=np.cos(2*PI*(data@dirs[i:i+128].T)/p['a']).mean(axis=0)
        return dirs[int(np.argmax(objective))]
    errors=[]
    J=np.array([[0.,-1.],[1.,0.]])
    for _ in range(8):
        axis_angle=float(RNG.uniform(0,PI));theta=float(RNG.uniform(-PI/8,PI/8))
        u=axis(sample(axis_angle,1500));v=axis(sample(axis_angle+theta,1500))
        estimate=math.atan(float((J@u)@v)/float(u@v))
        error=abs(estimate-theta);errors.append(error)
        require(error<.06,'seeded calibration/sensing demonstration')
    report['estimator_demo']={'dimension':2,'beta':beta,'gamma':gamma,'R':R,'copies_per_batch':1500,
             'trials':len(errors),'max_angle_error':max(errors),'errors':errors,
             'warning':'Low-dimensional illustration, not a cryptographically hard instance or proof of the sample theorem.'}
    report['assertions']=CHECKS
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true',help='write expected_results.json after all checks pass')
    args=parser.parse_args()
    report=run()
    text=json.dumps(report,indent=2,sort_keys=True)
    print(text)
    if args.write:
        Path(__file__).with_name('expected_results.json').write_text(text+'\n',encoding='utf-8')

if __name__=='__main__':
    main()
