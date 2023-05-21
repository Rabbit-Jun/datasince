"""
평균값 : 각 데이터를 더한 후 총 데이터 갯수로 나눈 대표값
극단적인 값에 매우 취약함
중앙값: 자료의 중앙에 있는 대표값
최빈값 : 가장 자주 나나타는 대표값
중요도는 값<변동성
값의 변동성은 값들이 평균을 중심으로 얼마나 모여있는지를 나타냄
분산: 각 데이터 값에서 평균을 뺀 값을 제곱하여 더한 뒤 데이터 수로 나눔
,즉 편차 제곱의 평균
표준편차: 분산에 제곱근을 취한 값
단, 데이터에서 일부를 추출한 표본에서
데이터 모집단의 분산을 추정할 때에는
표본 내에서 나타난 표본평균 대비 편차 제곱의 합을
(데이터 개수 -1)로 나누는 것이 적합한 추정치가 된다
"""
def space():
    print()
    print()
import pandas as pd
import numpy as np
b= pd.read_csv('buylov.csv')
print(b)
space()
print(b['BGiftPrice'])
#'BGiftPrice인 열 값
space()
bg=b[b['Role']=='Giver']
br=b[b['Role']=='Receiver']
print('<Giver>')
print(bg)
print('<Receiver>')
print(br)
"""
b[조건] 형식을 기억하면 쉽다
b['Role'] 'Role'열에서 값이 'Giver'인 열을 bg에 넣는다
"""
space()
price=b['BGiftPrice']
print('평균',np.mean(price))
#price 의 평균
space()
print('중앙값', np.median(price))
#price의 중앙값
"""
중앙값과 평균의 차이가 많이 난다= 극단적인 가격이 있어서
가격 분포가 한쪽으로 치우침
"""
space()
print('표준편차', np.std(price))
#price의 표준편차
#변동성, 즉 가격이  평균을 중심으로 표준편차만큼의 범위에 흔히 나타남


