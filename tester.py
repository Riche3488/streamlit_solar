import streamlit as st
#import psycopg2
import pandas as pd
import streamlit_autorefresh as st_autorefresh
# 데이터베이스 설정
host = "your_host"
dbname = "your_dbname"
user = "your_user"
password = "your_password"

# Streamlit 페이지를 주기적으로 새로 고침하는 시간 설정 (예: 10000ms = 10초)
refresh_time = 10000
st_autorefresh.st_autorefresh(interval=refresh_time)

# 데이터 불러오기
#data = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]}) #get_data()
data = pd.read_csv('test.csv')

# 데이터 표시
st.write("Updated Data:", data)
