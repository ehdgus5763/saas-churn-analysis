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

import matplotlib.pyplot as plt
import seaborn as sns

# 한글 깨짐 방지 (윈도우용 폰트 설정)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 그래프 1: 계약 유형별 이탈률
plt.figure(figsize=(8, 5))
contract_churn = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
contract_churn['Yes'].plot(kind='bar', color='coral')
plt.title('계약 유형별 이탈률')
plt.ylabel('이탈률')
plt.xlabel('계약 유형')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/contract_churn.png')
plt.show()

# 그래프 2: 가입기간별 이탈률
plt.figure(figsize=(8, 5))
tenure_churn = df.groupby('tenure_group')['Churn'].value_counts(normalize=True).unstack()
tenure_churn['Yes'].plot(kind='bar', color='skyblue')
plt.title('가입기간별 이탈률')
plt.ylabel('이탈률')
plt.xlabel('가입기간')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/tenure_churn.png')
plt.show()

# 그래프 3: 결제수단별 이탈률
plt.figure(figsize=(8, 5))
payment_churn = df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
payment_churn['Yes'].plot(kind='bar', color='mediumseagreen')
plt.title('결제수단별 이탈률')
plt.ylabel('이탈률')
plt.xlabel('결제수단')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('images/payment_churn.png')
plt.show()
