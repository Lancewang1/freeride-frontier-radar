import datetime
import json
import unittest
from pathlib import Path
from urllib.parse import urlparse,parse_qs
ROOT=Path(__file__).resolve().parents[1]


class SnapshotIntegrity(unittest.TestCase):
    def setUp(self):self.d=json.loads((ROOT/'landscape.json').read_text(encoding='utf-8'))

    def test_unique_ids_and_window(self):
        es=self.d['funding'];self.assertEqual(len({e['id'] for e in es}),len(es))
        for e in es:
            datetime.date.fromisoformat(e['date'])
            self.assertTrue(self.d['window']['start']<=e['date']<=self.d['window']['end'])
            self.assertEqual(len(e['source_hash']),64)
            self.assertTrue(e['url'].startswith('https://'))
            self.assertGreaterEqual(len(e['quote']),10)

    def test_fx_and_coarse_amounts(self):
        for e in self.d['funding']:
            if e['amount_kind']=='coarse':self.assertIsNone(e['amount']);self.assertIsNone(e['usd_m'])
            if e['currency']=='CNY' and e['amount'] is not None and e['status']=='completed':
                fx=self.d['fx'][e['date']];self.assertAlmostEqual(e['usd_m'],e['amount']/fx['rate'],places=5)
                self.assertLessEqual(fx['rate_date'],e['date'])

    def test_query_pairs_and_representative_records(self):
        for t in self.d['topics']:
            ps=[p for p in self.d['papers'] if p['topic']==t['id']]
            self.assertEqual({p['region'] for p in ps},{'cn','global'})
            self.assertEqual(len({p['query'] for p in ps}),1)
            for p in ps:
                self.assertGreaterEqual(p['count'],len(p['records']))
                self.assertIn('2025-10-01',parse_qs(urlparse(p['url']).query)['filter'][0])
                for r in p['records']:self.assertIn(urlparse(r['url']).scheme,('https','http'))

    def test_no_invented_fixture(self):
        self.assertFalse((ROOT/'radar.js').exists())
        self.assertNotIn('radarFixture',(ROOT/'landscape-ui.js').read_text(encoding='utf-8'))
        self.assertEqual(len(self.d['discussions']),12)


if __name__=='__main__':unittest.main()
