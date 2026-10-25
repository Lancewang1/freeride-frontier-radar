from playwright.sync_api import sync_playwright
from pathlib import Path
import os
import json
ROOT=Path(__file__).resolve().parents[1]/'test-results'
ROOT.mkdir(exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(channel='msedge');page=b.new_page(viewport={'width':1440,'height':1050});errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(os.environ.get('FR_DEMO_URL','http://127.0.0.1:8000'));page.wait_for_selector('#reading-ledger details',state='attached')
    assert page.locator('#deep-report h3').count()>=8
    assert page.locator('#landscape').is_visible()
    assert page.locator('#deepdive').is_visible()
    assert page.locator('#market').is_visible()
    assert page.locator('#landscape').evaluate('(e)=>!!(e.compareDocumentPosition(document.getElementById("deepdive")) & Node.DOCUMENT_POSITION_FOLLOWING)')
    assert page.locator('#reading-ledger details').count()==8
    page.locator('[data-view=reading]').click();assert page.locator('#paper-audit .source').count()==38
    page.locator('#paper-query').fill('SynFER');assert page.locator('#paper-audit .source').count()==1
    page.locator('[data-view=market]').click();assert page.locator('#market-results .metric').count()==6
    assert page.locator('#accounts').input_value()=='600'
    page.locator('#market-region').select_option('global');assert page.locator('#accounts').input_value()=='3000'
    page.locator('#qualified').fill('0');assert '0 ' in page.locator('#market-results .metric').nth(2).inner_text()
    page.locator('#qualified').fill('101');assert page.locator('#market-results .metric').count()==0
    page.locator('#market-region').select_option('cn')
    with page.expect_download() as event:page.locator('#export-market').click()
    event.value.save_as(ROOT/'market.json');assert json.loads((ROOT/'market.json').read_text())['outputs']['som']==2400000
    page.locator('[data-view=landscape]').click();page.wait_for_selector('#radar-topic')
    assert page.locator('#radar-cn .evidence-point').count()==3
    assert page.locator('#radar-global .evidence-point').count()==7
    assert page.locator('.funding-row').count()==22
    page.locator('#radar-global [data-point=synthetic] circle').click()
    assert page.locator('#radar-topic').input_value()=='synthetic'
    assert page.locator('.evidence-point.chosen').count()==2
    page.locator('#radar-drop').check()
    assert page.locator('.evidence-point.chosen').count()==0
    page.locator('#radar-drop').uncheck()
    page.locator('#radar-metric').select_option('count')
    assert page.locator('#radar-cn .evidence-point').count()==5
    page.locator('#radar-metric').select_option('amount')
    page.locator('#radar-topic').select_option('science');page.locator('#radar-strict').check()
    assert page.locator('.evidence-point.chosen').count()==0
    page.locator('#radar-strict').uncheck()
    page.locator('#ledger-scope').select_option('excluded');assert page.locator('.funding-row').count()==3
    page.locator('#ledger-scope').select_option('all');page.locator('#ledger-search').fill('Mem0');assert page.locator('.funding-row').count()==1
    page.locator('#ledger-search').fill('');
    with page.expect_download() as event:page.locator('#download-ledger').click()
    event.value.save_as(ROOT/'test-download.csv');assert len((ROOT/'test-download.csv').read_text(encoding='utf-8-sig').splitlines())==23
    with page.expect_download() as event:page.locator('#download-snapshot').click()
    event.value.save_as(ROOT/'test-download.json');assert len(json.loads((ROOT/'test-download.json').read_text(encoding='utf-8'))['funding'])==22
    page.locator('[data-view=deepdive]').click();assert page.locator('#landscape').is_visible();assert page.locator('#deep-report').is_visible()
    page.locator('[data-view=landscape]').click();page.locator('#radar-topic').select_option('synthetic');page.evaluate('scrollTo(0,0)')
    page.locator('[data-view=deepdive]').click();page.screenshot(path=str(ROOT/'desktop.png'),full_page=False);page.locator('[data-view=landscape]').click()
    page.locator('#radar-cn').scroll_into_view_if_needed();page.screenshot(path=str(ROOT/'charts.png'),full_page=False)
    page.set_viewport_size({'width':390,'height':844});page.evaluate('scrollTo(0,0)');assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.screenshot(path=str(ROOT/'mobile.png'),full_page=False)
    page.locator('#radar-cn').scroll_into_view_if_needed();page.screenshot(path=str(ROOT/'mobile-chart.png'),full_page=False)
    page.locator('[data-view=deepdive]').click();page.evaluate('scrollTo(0,0)');assert page.evaluate('document.documentElement.scrollWidth <= innerWidth');page.screenshot(path=str(ROOT/'deep-mobile.png'))
    page.locator('[data-view=market]').click();assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    assert not errors,errors
    print('PASS browser: default 3/7 plots; linked circles; count mode; exact/largest sensitivity; 22-row ledger; filters; CSV/JSON downloads; deep dive; 38 triaged papers; calculator; desktop/mobile; no JS errors')
    b.close()
