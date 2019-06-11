# todo-server  

[![CircleCI](https://circleci.com/gh/watashun00/todo-server/tree/master.svg?style=svg)](https://circleci.com/gh/watashun00/todo-server/tree/master)

- TODO 管理サービス用の HTTP サーバ
- TODO イベントを POST で登録，GET で取得できる
- POST，GET ともに，データは JSON でやりとりする

<br/>

\# イベント登録 API request  
POST /api/v1/event  
{"deadline": "2019-06-11T14:00:00+09:00", "title": "レポート提出", "memo": ""}

\# イベント登録 API response  
200 OK  
{"status": "success", "message": "registered", "id": 1}

400 Bad Request  
{"status": "failure", "message": "invalid date format"}


\# イベント全取得 API request  
GET /api/v1/event

\# イベント全取得 API response  
200 OK  
{"events": [
    {"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "レポート提出", "memo": ""},
    ...
]}

\# イベント1件取得 API request  
GET /api/v1/event/${id}

\# イベント1件取得 API response  
200 OK  
{"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "レポート提出", "memo": ""}

404 Not Found
