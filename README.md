## Python Protyping App Template

- **Client** : Streamlit
- **Server** : fastAPI

## Running

Set-up your python development environment  
(This template used python 3.10.12)
```
$ pip install -r requirements.txt
```
- Connect Client Server
    ```
    $ cd client && streamlit run app.py
    ```
    You can now view your client in your browser `localhost:8502`
- Connect fastAPI Server
    ```
    $ uvicorn server.main.py
    ```
    You can now view your server in your browser `localhost:8000`
- Server Docs (=Swagger)
    ```
    $ uvicorn server.main.py
    ```
    You can now view your swagger in your browser `localhost:8000/docs`
- Disconnect Server
    - Window OS & MacOS Shorcut : `Ctrl + C`
    ```
    $ ^C  Stopping...
    ```

## Structure

```bash
.
├── LICENSE
├── READNE.md
├── client
│   └── app.py # frontend 실행파일
├── requirements.txt # dependency 관리
└── server
    ├── __init__.py
    ├── main.py # backend 실행파일
    ├── router # 외부 API 혹은 기타 연결
    │   ├── __init__.py
    │   └── auth.py
    └── utils # 기능별 모듈
        ├── __init__.py
        └── chat.py
```

