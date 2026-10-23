import json
from pathlib import Path
import unittest
from collect import parse

ROOT = Path(__file__).resolve().parents[1]


class EvidenceIntegrity(unittest.TestCase):
    def test_all_claims_have_registered_sources(self):
        data = json.loads((ROOT / 'data.json').read_text(encoding='utf-8'))
        ids = {s['id'] for s in data['sources']}
        self.assertEqual(len(data['cases']), 3)
        for c in data['cases']:
            for f in c['facts']:
                self.assertIn(f['source'], ids)
                self.assertTrue(f['locator'])
            self.assertEqual(len(c['plan']), 4)
        for s in data['sources']:
            self.assertTrue(s['url'].startswith('https://'))
            if 'file' in s:
                self.assertEqual(len(s['sha256']), 64)

    def test_collector_rejects_external_entry_urls(self):
        xml = b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>javascript:bad</id><title>bad</title></entry><entry><id>http://arxiv.org/abs/1234.56789v1</id><title>A  title</title><summary>source text</summary></entry></feed>'
        out = parse(xml, 'audit')
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]['title'], 'A title')
        self.assertEqual(out[0]['status'], 'pending-research')


if __name__ == '__main__':
    unittest.main()
