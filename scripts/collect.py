"""Collect public arXiv metadata; never generate research conclusions."""
import datetime
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
QUERIES = {
    'audit': 'all:"selective auditing" OR all:"agent verification"',
    'revocation': 'all:"agent" AND (all:"revocation" OR all:"authorization")',
    'lab': 'all:"self-driving laboratories" OR all:"spectral analysis"',
}


def parse(raw, topic):
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(raw)
    items = []
    for e in root.findall('a:entry', ns):
        url = e.findtext('a:id', '', ns).replace('http://', 'https://')
        if not url.startswith('https://arxiv.org/abs/'):
            continue
        items.append({'id': url, 'url': url, 'title': ' '.join(e.findtext('a:title', '', ns).split()),
                      'summary': ' '.join(e.findtext('a:summary', '', ns).split()),
                      'published': e.findtext('a:published', '', ns), 'topic': topic,
                      'status': 'pending-research'})
    return items


def main():
    path = ROOT / 'pending.json'
    previous = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'items': []}
    items = {x['id']: x for x in previous['items']}
    errors = []
    for topic, query in QUERIES.items():
        params = urllib.parse.urlencode({'search_query': query, 'start': 0, 'max_results': 6,
                                        'sortBy': 'submittedDate', 'sortOrder': 'descending'})
        try:
            req = urllib.request.Request('https://export.arxiv.org/api/query?' + params,
                                         headers={'User-Agent': 'FREERIDE-Research-Demo/1.0'})
            with urllib.request.urlopen(req, timeout=40) as r:
                for item in parse(r.read(), topic):
                    old = items.get(item['id'])
                    if old and topic not in old['topic'].split(', '):
                        item['topic'] = old['topic'] + ', ' + topic
                    items[item['id']] = item
        except Exception as exc:
            errors.append(topic + ': ' + type(exc).__name__)
        time.sleep(3)
    batch = {'collected_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'queries': QUERIES, 'errors': errors,
             'items': sorted(items.values(), key=lambda x: x['published'], reverse=True)[:200]}
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Collected/preserved {len(batch['items'])} unique records; errors: {len(errors)}")
    if errors:
        print('; '.join(errors))


if __name__ == '__main__':
    main()
