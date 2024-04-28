## Python Protype Template

- **Client** : streamlit
- **Server** : fastAPI


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