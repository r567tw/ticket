from playwright.sync_api import sync_playwright
import os
import time
from twocaptcha import TwoCaptcha
from dotenv import load_dotenv


def get(pid,startStation,endStation,rideDate,trainNoList1,trainNoList2=None,trainNoList3=None):
    app_start_time = time.time()

    url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query"
    
    api_key = os.getenv('CAPTCHA_API_KEY')

    with sync_playwright() as playwright:
        browser_type = playwright.chromium  # 選擇瀏覽器類型，這裡使用 Chromium
        
        # 啟動瀏覽器並創建上下文
        # browser = browser_type.launch(headless= False)
        browser = browser_type.launch()
        context = browser.new_context()

        # 創建新頁面
        page = context.new_page()
        
        # 最大化視窗
        # page.maximize()

        # 前往網址
        page.goto(url)

        # 進行元素定位和操作
        page.fill("#pid", pid)
        page.fill("#startStation", startStation)
        page.fill("#endStation", endStation)
        # 我這裡還是要注意一下時間有沒有寫對！不然台鐵會驗證擋掉...
        page.fill("#rideDate1", rideDate)
        page.fill("#trainNoList1", trainNoList1)
        if trainNoList2 != None:
            page.fill("#trainNoList2", trainNoList2)
        if trainNoList3 != None:
            page.fill("#trainNoList2", trainNoList3)

        # recaptcha 處理
        recaptcha = page.query_selector('div.g-recaptcha')
        if recaptcha:
            recaptcha_key = recaptcha.get_attribute('data-sitekey')
            # print(recaptcha_key)
        
        start_time = time.time()

        solver = TwoCaptcha(api_key)

        try:
            # 這裡要等人解開...
            result = solver.recaptcha(
                sitekey=recaptcha_key,
                url=url,
            )

            end_time = time.time()
            TwoCaptcha_time = end_time - start_time
            # trace
            print(f"2Captcha took {TwoCaptcha_time:.2f} seconds to execute.")

            # 印出 recaptcha 解決結果
            # print(result)

            # 這裡很奇怪, 一定要將這個元素改成 visable 才能破解 recaptcha
            page.eval_on_selector(
                selector="textarea[id=g-recaptcha-response]",
                expression="(el) => el.style.display = 'inline-block'",
            )
        except:
            return "Result: 取票失敗，請手動取票。"


        textarea = page.locator("textarea[id=g-recaptcha-response]")
        textarea.fill(result["code"])
        page.click("input[type=submit]")
        
        # 新寫法: 偏向使用這個 等待某個元素出現在擷取文字！
        element = page.wait_for_selector('.cartlist-id', timeout=5000)
        
        # 截圖存起來, 算是方便之後trace or debug
        page.screenshot(path='screenshot.png')
        result = element.text_content()
        # print(result)
        
        # 關閉瀏覽器
        context.close()

    app_end_time = time.time()
    app_time = app_end_time - app_start_time
    # trace
    print(f"This App took {app_time:.2f} seconds to process.")

    # Line notify result ...
    return "Result:{}".format(result)

