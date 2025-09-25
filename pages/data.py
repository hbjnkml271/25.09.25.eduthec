years = list(range(2000, 2026))
months = list(range(1, 13))
st.markdown('---')
# 기간 선택창: 시작 년/월, 종료 년/월
st.subheader('기간별 코스피 평균 조회')
col1, col2, col3, col4 = st.columns(4)
with col1:
	start_year = st.selectbox('시작 년도', years, index=0, key='start_year')
with col2:
	start_month = st.selectbox('시작 월', months, index=0, key='start_month')
with col3:
	end_year = st.selectbox('종료 년도', years, index=len(years)-1, key='end_year')
with col4:
	end_month = st.selectbox('종료 월', months, index=11, key='end_month')

# 임의의 월별 코스피 데이터 전체 생성 (2000~2025, 1~12월)
all_monthly_kospi = {(y, m): random.randint(800, 3500) for y in years for m in months}

# 선택된 기간의 (년도, 월) 리스트 생성
def get_period_list(start_y, start_m, end_y, end_m):
	period = []
	for y in range(start_y, end_y + 1):
		m_start = start_m if y == start_y else 1
		m_end = end_m if y == end_y else 12
		for m in range(m_start, m_end + 1):
			period.append((y, m))
	return period

selected_period = get_period_list(start_year, start_month, end_year, end_month)
selected_values = [all_monthly_kospi[(y, m)] for (y, m) in selected_period]

if selected_values:
	avg_kospi = np.mean(selected_values)
	st.info(f"{start_year}년 {start_month}월 ~ {end_year}년 {end_month}월 코스피 평균: {avg_kospi:.2f}")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import datetime
import random

# 예시 데이터 생성
data = {
	'과목': ['수학', '영어', '과학', '역사', '미술'],
	'점수': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = '../fonts/NanumGothic-Regular.ttf'
font_manager.fontManager.addfont(font_path)
rc('font', family='NanumGothic')

# Streamlit 페이지: 년도 선택 및 코스피 데이터 표시
st.title('년도별 코스피 지수 조회')

# 임의의 코스피 데이터 생성 (2000~2025)
years = list(range(2000, 2026))
kospi_data = {year: random.randint(800, 3500) for year in years}

# 년도 선택창
selected_year = st.selectbox('년도를 선택하세요', years, index=len(years)-1)

# 선택된 년도의 코스피 값 표시
st.subheader(f"{selected_year}년 코스피 지수")
st.write(f"코스피: {kospi_data[selected_year]}")

# 코스피 변화 그래프
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(years, [kospi_data[y] for y in years], marker='o', color='green')
ax.set_xlabel('년도')
ax.set_ylabel('코스피')
ax.set_title('년도별 코스피 지수 변화')
plt.tight_layout()
st.pyplot(fig)

# 월 선택창 및 월별 코스피 변화 그래프
months = list(range(1, 13))
selected_month = st.selectbox('월을 선택하세요', months, index=0)

# 임의의 월별 코스피 데이터 생성 (해당 년도 기준)
monthly_kospi = [random.randint(800, 3500) for _ in months]

st.subheader(f"{selected_year}년 {selected_month}월 코스피 추이")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(months, monthly_kospi, marker='o', color='blue')
ax2.set_xticks(months)
ax2.set_xlabel('월')
ax2.set_ylabel('코스피')
ax2.set_title(f'{selected_year}년 월별 코스피 지수 변화')
plt.tight_layout()
st.pyplot(fig2)
# 막대그래프 생성 및 저장
plt.figure(figsize=(8, 5))
plt.bar(df['과목'], df['점수'], color='skyblue')
plt.xlabel('과목')
plt.ylabel('점수')
plt.title('학생 점수 분포')
plt.tight_layout()
plt.savefig('simple_bar_chart.png')  # 그래프 파일로 저장
plt.close()
