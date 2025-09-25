# 간단한 데이터 그래프 생성 예시
import pandas as pd
import matplotlib.pyplot as plt

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

# 막대그래프 생성 및 저장
plt.figure(figsize=(8, 5))
plt.bar(df['과목'], df['점수'], color='skyblue')
plt.xlabel('과목')
plt.ylabel('점수')
plt.title('학생 점수 분포')
plt.tight_layout()
plt.savefig('simple_bar_chart.png')  # 그래프 파일로 저장
plt.close()
