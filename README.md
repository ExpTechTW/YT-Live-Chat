# trem-report-limit-plugin
一個用來紀錄 YT直播聊天室 的 Python 工具

## 索引
- [使用說明](#使用說明)
- [貢獻者](#貢獻者)
- [發佈規則](#發佈規則)
- [合作](#合作)

## 使用說明
- 安裝所需要的模組 `requirements.txt`
- 設定 `config.json`

> `video_id` 為 YouTube 直播網址中的一段唯一識別碼

> `webhook_url` 為 發送到對應的頻道

### 取得 YouTube 直播 Video ID 說明
1. 開啟 YouTube 直播網頁
2. 在網址列中找到 "v=" 後面的字串

   例如：https://www.youtube.com/watch?v=abcd1234xyz
   
   其中 "abcd1234xyz" 就是 Video ID

### Discord Webhook URL 設定說明
1. 在 Discord 伺服器中開啟想要接收 YouTube 聊天室訊息的文字頻道
2. 右鍵點擊頻道 > 編輯頻道
3. 點擊「整合」
4. 點擊「建立 Webhook」
5. 設定 Webhook 名稱（選擇性）
6. 複製產生的 Webhook URL
7. 將複製的 URL 貼到 config.json 的 webhook_url 欄位

## 貢獻者
- bamboo0403 

------

## 發佈規則
- 如果新版本中有錯誤，且尚未列出，請將錯誤資訊提交到 ```issue```
- 如果您使用任何形式的辱罵性或貶義性語言給其他用戶，您將永遠被封禁！
- 不要發送重複無意義內容至 ```issue```，否則您將永遠被封禁！
- 若有任何問題或建議，歡迎提出

## 合作
- 若有任何可以改進的地方，歡迎使用 ```Pull requests``` 來提交
