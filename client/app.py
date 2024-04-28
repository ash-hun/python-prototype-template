import streamlit as st
import pandas as pd
from datetime import datetime
import requests

st.title('MVP')

# 로그아웃 API (http://localhost:8501로 리다이렉트)
# logout_button_html = '<a href="http://localhost:8000/logout" target="_self">Logout</a>'

# 쿼리 파라미터에서 유저 정보 확인 (이메일)
# user_info = st.query_params.get_all('user_info')
# if user_info:
#     st.session_state['user_info'] = user_info[0]

# 로그인 상태
# if 'user_info' in st.session_state:
#     st.success(f'Logged in as {st.session_state["user_info"]}')
#     st.markdown(logout_button_html, unsafe_allow_html=True)

#     # 코인 가격 정보 조회 API 
#     def get_current_prices():
#         ...
#         return data

#     # session_state 변수 초기화    
#     if 'price_data' not in st.session_state:
#         st.session_state.price_data = pd.DataFrame(columns=['market', 'trade_date', 'trade_timestamp', 'high_price', 'low_price', 'trade_price'])
#     if 'latest_price' not in st.session_state:
#         st.session_state.latest_price = pd.DataFrame()

#     # 현재 시세 확인 후 session_state.latest_price에 저장
#     if st.button('현재 시세 확인'):
#         data = get_current_prices()
#         price_data = pd.DataFrame(data)
#         st.session_state.latest_price = price_data[['market', 'trade_date', 'trade_timestamp', 'high_price', 'low_price', 'trade_price']]

#     # 현재 시세 확인 테이블 출력
#     st.header("암호화폐 시세")
#     if not st.session_state.latest_price.empty:
#         st.table(st.session_state.latest_price)

#     st.header("비트코인 가격 기록")

#     # 버튼을 누르면 BTC 정보 기록 한 줄 씩 concat
#     if st.button('BTC 정보 기록'):
#         if not st.session_state.latest_price.empty:
#             btc_data = st.session_state.latest_price[st.session_state.latest_price['market'] == 'KRW-BTC']
#             if not btc_data.empty:
#                 st.session_state.price_data = pd.concat([st.session_state.price_data, btc_data], ignore_index=True)

#     # BTC 정보 기록 테이블
#     st.table(st.session_state.price_data)

# # 비 로그인 상태
# else:
#     login_button_html = '<a href="http://localhost:8000/login" target="_blank">Login with Google</a>'
#     st.markdown(login_button_html, unsafe_allow_html=True)
#     if not user_info:
#         st.error('Not logged in or logged out')