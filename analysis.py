import pandas as pd

# 데이터 불러오기
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 데이터 첫 5줄 보기
print(df.head())

# 데이터 기본 정보 보기 (컬럼 개수, 데이터 타입, 결측치)
print(df.info())

# 이탈률 전체 확인
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True))

# 계약 유형별 이탈률 (질문1)
# Month-to-month, One year, Two year 계약별로 이탈률이 어떻게 다른지  
print(df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack())

#tenure(가입구간) 구간 나누기 (질문2)
df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 60, 72], labels=['0-12개월', '12-24개월', '24-36개월', '36-48개월', '48-60개월', '60-72개월'])
print(df.groupby('tenure_group')['Churn'].value_counts(normalize=True))

# 결제수단별 이탈률(질문3)      
print(df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True))

# 이탈고객 vs 잔존 고객 요금 비교 (질문4)
print(df.groupby('Churn')['MonthlyCharges'].mean())


