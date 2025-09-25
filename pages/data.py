# 간단한 데이터 그래프 생성 예시
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
# 막대그래프 생성 및 저장
plt.figure(figsize=(8, 5))
plt.bar(df['과목'], df['점수'], color='skyblue')
plt.xlabel('과목')
plt.ylabel('점수')
plt.title('학생 점수 분포')
plt.tight_layout()
plt.savefig('simple_bar_chart.png')  # 그래프 파일로 저장
plt.close()
