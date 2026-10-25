"""Refresh query counts into private pending data; never overwrite reviewed scores."""
import datetime
import json
import time
import urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def main():
    snapshot=json.loads((ROOT/'landscape.json').read_text(encoding='utf-8'))
    result={'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'pending-review','results':[],'errors':[]}
    for item in snapshot['papers']:
        try:
            req=urllib.request.Request(item['url'],headers={'User-Agent':'FREERIDE-Research/0.4'})
            with urllib.request.urlopen(req,timeout=30) as response:data=json.load(response)
            result['results'].append({'topic':item['topic'],'region':item['region'],'url':item['url'],'count':data['meta']['count'],'raw':data})
        except Exception as error:
            result['errors'].append({'topic':item['topic'],'region':item['region'],'error':type(error).__name__,'message':str(error)})
            if getattr(error,'code',None)==429:break
        time.sleep(1)
    target=ROOT/'private';target.mkdir(exist_ok=True)
    (target/'landscape-pending.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"Pending records: {len(result['results'])}; errors: {len(result['errors'])}. Reviewed snapshot unchanged.")


if __name__=='__main__':main()
