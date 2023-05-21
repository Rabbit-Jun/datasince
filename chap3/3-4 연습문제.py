"""
np.max()와 np.argmax()의 차이를 예를 들어 설명하시오
"""
import numpy as np
a=np.array([[1,3],[4,5]])
print(a)
print(np.max(a))
print(np.argmax(a))
#np.max는 최댓값을 반환하고 np.argmax는 최대값이 있는 인덱스 값을 반환
