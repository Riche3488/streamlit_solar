import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# matplotlib에서 한글 폰트 설정
plt.rc('font', family='Malgun Gothic') # Windows의 경우
# plt.rc('font', family='AppleGothic') # macOS의 경우
plt.rc('axes', unicode_minus=False) # 축에서 마이너스 기호가 깨지지 않도록 설정

# 임시 데이터 생성
def generate_hourly_data():
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    times = [today + timedelta(hours=i) for i in range(24)]
    values = [np.random.randint(0, 100) for _ in range(24)]
    return pd.DataFrame({'시간': times, '발전량': values})

def generate_cumulative_data():
    dates = [datetime.now() - timedelta(days=i) for i in range(30)]
    cum_values = np.cumsum([np.random.randint(20, 50) for _ in range(30)])
    return pd.DataFrame({'날짜': dates, '누적 발전량': cum_values})



# 데이터 로드
hourly_data = generate_hourly_data()
cumulative_data = generate_cumulative_data()

# 탭 생성
tab1, tab2, tab3 = st.tabs(["오늘의 발전량", "누적 발전량", "PDF 보기"])

# 첫 번째 탭: 시간대별 발전량 및 신호등
with tab1:
    # 최근 발전량에 따른 신호등
    st.markdown(f'<div style="color: green; font-size: 24px;">●</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write("오늘의 시간대별 발전량")
        st.dataframe(hourly_data)
    with col2:
        # 그래프 그리기
        fig, ax = plt.subplots()
        ax.plot(hourly_data['시간'], hourly_data['발전량'], marker='o', linestyle='-')
        ax.set_xlabel('시간')
        ax.set_ylabel('발전량')
        ax.set_title('시간별 발전량')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# 두 번째 탭: 누적 발전량
with tab2:
    st.write("날짜별 누적 발전량")
    st.dataframe(cumulative_data)

    # 그래프 그리기
    fig, ax = plt.subplots()
    ax.plot(cumulative_data['날짜'], cumulative_data['누적 발전량'], marker='o', linestyle='-')
    ax.set_xlabel('날짜')
    ax.set_ylabel('누적 발전량')
    ax.set_title('날짜별 누적 발전량')
    plt.xticks(rotation=45)
    st.pyplot(fig)


# 새 탭3: PDF 보기
with tab3:
    st.write("PDF 파일 보기")


