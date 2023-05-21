import pandas as pd
from sklearn import datasets
dataset=datasets.load_wine()
import matplotlib.pyplot as plt
"""
print(dataset.DESCR)
  
#데이터셋의 속성 종류 출력
print(dir(dataset))
#data 속성만 출력하기
print(dataset.data)

print("data type=", type(dataset.data)) #<class 'numpy.ndarray>
print("data shape=", dataset.data.shape)#(178, 13)
print("first row of data=", dataset.data[0])#데이터 첫번째 줄 출력 표기법으로 표현

#지수적 표기법
#1.2e+0.5 는 1.2에 10**5, 120000

print("feature name=", dataset.feature_names)
print("target=", dataset.target)
print("target names=", dataset.target_names)
#기계학습을 위한 기본 구조
# 각각의 와인은 13개의 특성과 1개의 정답을 가지고 있음
#특성과 정답으로 구성된 각각의 와인 데이터를 데이터포인트라고 함
#데이터 포인트들을 대량으로 모아놓은 것은 데이터 셋
"""
d=pd.DataFrame(dataset.data, columns=dataset.feature_names)
#새로운 데이터프레임을 생성
d['target'] =dataset.target
#target이라는 새로운 열을 추가하고 그 값으로 datasets.target의 값을 넣음
plt.scatter(d['alcohol'],d['malic_acid'])
plt.xlabel('alcohol')
plt.ylabel('malic_acid')
plt.show()
