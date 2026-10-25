from playwright.sync_api import sync_playwright
from pathlib import Path
import os
import json
ROOT=Path(__file__).resolve().parents[1]/'test-results'
ROOT.mkdir(exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(channel='msedge');page=b.new_page(viewport={'width':1440,'height':1050});errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(os.environ.get('FR_DEMO_URL','http://127.0.0.1:8000'));page.wait_for_selector('#radar-topic')
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
    page.locator('[data-view=research]').click();assert page.locator('#landscape').is_hidden();assert page.locator('.card').count()==3
    page.locator('[data-tab=market]').click();assert page.locator('#calc .metric').count()==3
    page.locator('[data-view=landscape]').click();page.locator('#radar-topic').select_option('synthetic');page.evaluate('scrollTo(0,0)')
    page.screenshot(path=str(ROOT/'desktop.png'),full_page=False)
    page.locator('#radar-cn').scroll_into_view_if_needed();page.screenshot(path=str(ROOT/'charts.png'),full_page=False)
    page.set_viewport_size({'width':390,'height':844});page.evaluate('scrollTo(0,0)');assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.screenshot(path=str(ROOT/'mobile.png'),full_page=False)
    page.locator('#radar-cn').scroll_into_view_if_needed();page.screenshot(path=str(ROOT/'mobile-chart.png'),full_page=False)
    assert not errors,errors
    print('PASS browser: default 3/7 plots; linked circles; count mode; exact/largest sensitivity; 22-row ledger; filters; CSV/JSON downloads; archive; desktop/mobile; no JS errors')
    b.close()
