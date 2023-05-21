import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b=pd.read_csv('buylov.csv')
bp=b['BGiftPrice']
plt.hist(bp)
plt.show()
#hist()는 가로축에는 데이터 값의 범위를,  세로축에는 해당 값의 빈도수준을 나타냄
plt.boxplot(bp)
plt.show()
"""
상자 그림(Box Plot)은 데이터의 분포를 시각화하는 그래프 중 하나입니다. 상자 그림에서 IQR(Interquartile Range)는 데이터의 중간 50%에 대한 범위를 나타내는 값입니다. IQR은 이상치(outlier)를 탐지하거나 데이터의 분포를 이해하는 데 도움이 됩니다.

IQR을 구하는 방법은 다음과 같습니다.

데이터를 크기 순서대로 정렬합니다.
데이터 개수가 홀수이면 중앙값을 제외한 데이터를 두 개의 그룹으로 나눕니다. 데이터 개수가 짝수이면 중앙값을 포함한 데이터를 두 개의 그룹으로 나눕니다.
각 그룹에서 1사분위수(Q1)와 3사분위수(Q3)를 구합니다.
IQR은 Q3에서 Q1을 빼서 구합니다.
수식으로 표현하면 다음과 같습니다.

IQR = Q3 - Q1

여기서, Q1은 하위 25%에 해당하는 값, Q3은 상위 25%에 해당하는 값입니다.

예를 들어, 데이터가 {1, 2, 3, 4, 5, 6, 7, 8, 9}이라면,

데이터를 정렬하면 {1, 2, 3, 4, 5, 6, 7, 8, 9}가 됩니다.
중앙값은 5이므로, 데이터를 {1, 2, 3, 4}와 {6, 7, 8, 9}로 나눕니다.
각 그룹에서 Q1은 2, Q3은 8입니다.
IQR은 Q3 - Q1 = 6 입니다.
1사분위수(Q1)에서 1.5 * IQR(IQR은 Interquartile Range, 즉 Q3 - Q1)을 뺀 값보다
작은 값 또는 Q3에서 1.5 * IQR을 더한 값보다 큰 값은 이상치로 간주합니다.
강력히 의심되는 값은 3*IQR

"""
bg=b[b['Role']=='Giver']
br=b[b['Role']=='Receiver']
print('<준 사람 선물가격>')
print('평균 :',np.mean(bg['BGiftPrice']))
print('중앙값 :',np.median(bg['BGiftPrice']))
print('<받은 사람 선물가격>')
print('평균 :',np.mean(br['BGiftPrice']))
print('중앙값 :',np.median(br['BGiftPrice']))
plt.boxplot([bg['BGiftPrice'],br['BGiftPrice']],labels=['Giver','Reicever'])
plt.show()
# [ 데이터프레임, 데이터프레임1] ,labels
print(bg['BGiftPrice'])
