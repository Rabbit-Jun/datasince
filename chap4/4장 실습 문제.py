"""
광역시도별 인구를 나타내고 있는 예제 데이터파일 'population.csv'를 활용하여
다음 물음에 답하시오

1) 전국 광역시도별 인구의 평균값과 중앙값을 구하고, 이 차이의 시사점을 설명하시오
2) 전국 광역시도별 인구의 표준편차를 구하고, 이 값의 시사점을 설명하시오
"""
import pandas as pd
import numpy as np

data =pd.read_csv('population.csv')
print(data)
print('광역시도별 인구의 평균값',np.mean(data['population']))
print('광역시도별 인구의 중앙값',np.median(data['population']))


#평균값이 중앙값의 약 2배에 도달한다는 것은 인구가 어느 특정 지역에 많이 몰려 있고
#나머지는 중앙값에 비슷하게 몰려 있을 거라고 추측할 수 있다


print('광역시도별 인구의 표준편차',np.std(data['population']))

#평균이 310십만 인데 표준편차가 336십만이라는 것은 데이터 값이 큰것은 646십만이고
#작은 것은 -26만 이라는 건데 평균보다 훨씬 멀리 떨어져 있는 값들이 존재하여
#데이터 분석의 신뢰성을 떨어뜨린다

"""
위의 데이터에서 전국 광역시도별 남녀 인구 비율의 평균값과 중앙값을 구하고,
이 차이의 시사점을 설명하시오
"""


ratio=[]
for i in range(len(data)):
    male=data.iloc[i]['male']
    female=data.iloc[i]['female']
    ratio.append(male/female)
print('남녀 비율 평균값',np.mean(ratio))
print('남녀 비율 중앙값',np.median(ratio))

#남녀 비율이 평균값과 중앙값이 비슷한 걸로 보아 각 시도별로 남녀 비율은 비슷하다
#고 추측할 수 있다
