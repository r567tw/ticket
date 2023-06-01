from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
import time
from twocaptcha import TwoCaptcha




load_dotenv()
url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query"
pid = os.environ.get('pid')
api_key = os.environ.get('CAPTCHA_API_KEY')

solver = TwoCaptcha(api_key)


with sync_playwright() as playwright:
    browser_type = playwright.chromium  # 選擇瀏覽器類型，這裡使用 Chromium
    
    # 啟動瀏覽器並創建上下文
    browser = browser_type.launch(headless= False)
    context = browser.new_context()

    # 創建新頁面
    page = context.new_page()
    
    # 最大化視窗
    # page.maximize()

    # 前往網址
    page.goto(url)

    # 進行元素定位和操作
    page.fill("#pid", pid)
    page.fill("#startStation", "1000-臺北")
    page.fill("#endStation", "6000-臺東")
    page.fill("#trainNoList1", "72")
    # recaptcha 真的是一大難關...
    
    recaptcha = page.query_selector('div.g-recaptcha')
    if recaptcha:
        recaptcha_key = recaptcha.get_attribute('data-sitekey')
        print(recaptcha_key)

    result = solver.recaptcha(
        sitekey=recaptcha_key,
        url="https://naweeklytimes.com/login-2/",
        version="v2",
    )

    page.eval_on_selector(
        selector="textarea[name=g-recaptcha-response]",
        expression="(el) => el.style.display = 'inline-block'",
      )
    textarea = page.locator("textarea[name=g-recaptcha-response]")
    textarea.fill(result['code'])
    page.click("input[type=submit]")
      
    time.sleep(10)
    page.pause()
    # page.click("#recaptcha-anchor")
    # 關閉瀏覽器
    context.close()
time.sleep(10)
