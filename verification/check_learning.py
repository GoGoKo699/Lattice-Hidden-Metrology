#!/usr/bin/env python3
"""Check the shared learning map and its worked example.

Run from any directory with the dependencies in requirements.txt. This checks
structural invariants and displayed calculations, not comprehension, hardness,
complete proof correctness, or GitHub's hosted mathematical rendering.
"""
from __future__ import annotations
import math
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

from verify import parameters

ROOT = Path(__file__).resolve().parents[1]
LEARNING = ROOT / 'learning'
MAP = (LEARNING / 'MILESTONES.md').read_text(encoding='utf-8')
BRIDGE = (LEARNING / 'PEIKERT_BRIDGE.md').read_text(encoding='utf-8')
BLOCKS = re.findall(r'^### M(\d{2}) — [^\n]+\n(.*?)(?=^### M\d{2}|\Z)', MAP,
                    flags=re.M | re.S)


def heading_slug(text: str) -> str:
    """GitHub-compatible slugs for the plain-text bridge headings used here."""
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


class LearningChecks(unittest.TestCase):
    def test_exact_map_and_allocation(self):
        self.assertEqual([int(i) for i, _ in BLOCKS], list(range(1, 31)))
        self.assertEqual(MAP.count('**Phase:** Background/preliminaries.'), 15)
        self.assertEqual(MAP.count('**Phase:** Narrative/innovation.'), 15)

    def test_record_fields(self):
        for i, text in BLOCKS:
            for field in ('Phase', 'Central question', 'Understanding target',
                          'Dependencies and story role', 'Conceptual connection',
                          'Source pointers'):
                with self.subTest(milestone=i, field=field):
                    self.assertEqual(len(re.findall(r'\*\*' + re.escape(field)
                                                    + r':\*\*', text)), 1)

    def test_dependencies_point_backward(self):
        for i, text in BLOCKS:
            dep = re.search(r'\*\*Dependencies and story role:\*\* ([^\n]+)', text)
            self.assertIsNotNone(dep)
            ids = [int(j) for j in re.findall(r'M(\d{2})', dep.group(1))]
            for low, high in re.findall(r'M(\d{2})–M(\d{2})', dep.group(1)):
                ids.extend(range(int(low), int(high) + 1))
            self.assertTrue(all(0 < j < int(i) for j in ids), (i, ids))
            if i == '01':
                self.assertIn('None;', dep.group(1))
            else:
                self.assertTrue(ids)

    def test_internal_learning_links(self):
        # Science and verification links are intentionally outside this check.
        # The repository-path inventory is audited separately in final review.
        for path in LEARNING.glob('*.md'):
            text = path.read_text(encoding='utf-8')
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                parts = urlsplit(target)
                if parts.scheme or parts.netloc:
                    continue
                dest = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                if dest.parent != LEARNING.resolve():
                    continue
                self.assertTrue(dest.is_file(), target)
                if parts.fragment:
                    heads = re.findall(r'^#{1,6} (.+)$', dest.read_text(encoding='utf-8'), re.M)
                    self.assertIn(unquote(parts.fragment), {heading_slug(h) for h in heads}, target)

    def test_anchor_version_is_explicit(self):
        self.assertIn('17 February 2016', BRIDGE)
        self.assertIn('18 February 2016', BRIDGE)
        self.assertIn('https://eprint.iacr.org/2015/939', BRIDGE)
        self.assertIn('not attributed to the 2016 survey', BRIDGE)

    def test_width_and_noise_conversion(self):
        p = parameters(.2, 3., 15.)
        self.assertAlmostEqual((p['c2'] - p['b2'])/(2*math.pi), .5/15**2)
        self.assertAlmostEqual(p['a'], .3318584, places=7)
        self.assertAlmostEqual(p['b2'], .00442478, places=8)
        self.assertAlmostEqual(p['c2'], .01838741, places=8)
        self.assertAlmostEqual(p['r2'], .166961, places=6)

    def test_contrast_and_photon_values(self):
        p = parameters(.2, 3., 15.)
        true_contrast = math.exp(-math.pi*p['r2'])
        perpendicular = math.exp(-math.pi*p['h2']/p['a']**2)
        self.assertAlmostEqual(true_contrast, .591837, places=6)
        self.assertTrue(math.isclose(perpendicular, 2.7431e-13, rel_tol=5e-6))
        pulse = 2*15**2/(4*math.pi)
        self.assertAlmostEqual(pulse, 35.8099, places=4)
        self.assertAlmostEqual(3000*pulse, 107430, delta=1)

    def test_sign_invariant_angle(self):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                u = (s1*math.cos(.6), s1*math.sin(.6))
                v = (s2*math.cos(.8), s2*math.sin(.8))
                numerator = -u[1]*v[0] + u[0]*v[1]
                denominator = u[0]*v[0] + u[1]*v[1]
                self.assertAlmostEqual(math.atan(numerator/denominator), .2)

    def test_calibration_cost_and_fraction(self):
        nc = ns = 1500
        self.assertEqual(nc*ns/(nc+ns), (nc+ns)/4)
        self.assertAlmostEqual(math.pi/(2*(1+math.pi)), .3792734964973881)


if __name__ == '__main__':
    unittest.main(verbosity=2)
