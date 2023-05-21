"""
'buylov.csv'데이터를 성별로 구분하여 각 성별의 선물가격에 대한 평균,중앙값,
표준편차를 구하여 비교하시오
"""
import pandas as pd
import numpy as np
data=pd.read_csv('buylov.csv')
print(data)

m=data.loc[data['Gender']=='Male']['BGiftPrice']
f=data.loc[data['Gender']=='Female']['BGiftPrice']
print('남자 평균',np.mean(m))
print('남자 중앙값',np.median(m))
print('남자 표준편차',np.std(m))
print('여자 평균',np.mean(f))
print('여자 중앙값',np.median(f))
print('여자 표준편차',np.std(f))
