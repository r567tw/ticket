# Ticket

## Used Technology
- `Python`
- `Line Notify`
- `2captcha`
- `Playwright`

## Pre Requirements
- Must Have `line notify token` & `2captcha API key`
- pip install -r requirements.txt
- playwright install chromium

## Line Notify
- inspire by Project `Jarvis`。We use line notify result to you.
- you can apply line-notify token using https://notify-bot.line.me/my/

## 使用範圍
- TRA: 台鐵搶票

## 未來計劃
- [V] 優化程式碼：看是否要抽換成一個可用的模組調用、台鐵一些參數抽上來做`env`提供他人客製化
- [ ] 增加其他網站訂票
- [ ] 程式trigger方案: 固定某個時間 在trigger 某個程式... no repeat
- [ ] 程式執行的 Log 收集與存放- 以便後續 trace
- [ ] 如果在訂票網站不太行的時候，不知道這些程式是否壞掉？(壓測)
<!-- gh secret set -f .env  // ifttt 是每天的一個工具...好像不太需要這樣用 -->

