"""
Numpy에는 정렬을 위한 두 가지의 함수 np.sort()와 np.argsort()가 있다.
둘 사이의 차이점을 설명하고 두 기능을 적절히 활용하여 다음의 두 numpy배열에서
점수의 내림차순으로 이름(names)를 출력하는 프로그램을 작성하시오
1 names= np.array(['A','B','C','D','E'])
2 scores =np.array([10,8,6,9,7], dtype='int32')
"""
#np.sort()는 원래 배열에서 순서를 오름차순으로 재 배열한 값을 반환한다
#np.argsort()는 원래 배열의 인덱스 값을 오름차순으로 재 배열된 모습으로 반환한다


import numpy as np
names= np.array(['A','C','B','D','E'])
scores =np.array([10,8,6,9,7], dtype='int32')

decreasing=np.argsort(-scores)
print(names[decreasing])

a=[0,1,2]
b=['apple','banana','tomato']
"""
print(b[a])는 타입 에러가 나온다
그 이유는 정수또는 슬라이스만 인덱싱이 가능하기때문
"""
c=[b[i] for i in a]
print(c)
