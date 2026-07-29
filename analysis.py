import pandas as pd

# 데이터 불러오기
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 데이터 첫 5줄 보기
print(df.head())

# 데이터 기본 정보 보기 (컬럼 개수, 데이터 타입, 결측치)
print(df.info())
