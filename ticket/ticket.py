# 去 自強(3000) 385  禮拜三晚上八點~十點
# # 暫支援class id name
# from selenium import webdriver
# from time import sleep
# import json


# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)
# browser.find_element_by_id("startStation").send_keys("1000-臺北")
# browser.find_element_by_id("endStation").send_keys("6000-臺東")
# browser.find_element_by_id("trainNoList1").send_keys("72")
# browser.find_element_by_id("recaptcha-anchor-label").click()

from playwright.sync_api import sync_playwright

url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query"
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
    page.fill("#pid", "")
    page.fill("#startStation", "1000-臺北")
    page.fill("#endStation", "6000-臺東")
    page.fill("#trainNoList1", "72")
    # recaptcha 真的是一大難關...
    
    div_element = page.query_selector('div.g-recaptcha')
    if div_element:
        div_property = div_element.get_attribute('data-sitekey')
        print(div_property)

    page.click("#recaptcha-anchor")
    page.click("#recaptcha-anchor")

    # 關閉瀏覽器
    context.close()
