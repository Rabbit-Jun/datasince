import numpy as np
#numpy 패키지를 import 해서 np라고 부르자
def space():
    print()
    print()
    
a1 =[2,3,5]
print(a1)
a2=np.array(a1)
print(a2)
# 리스트a1을 numpy 형식으로 배열 하라
print(type(a2))
#a2의 타입을 확인하라
print(a2.shape)
#a2의 크기를 확인하라 
a2[0]=7
print(a2)
# a2[0]에 7을 넣어주셈
space()
c= np.array([1,2,3])
d= np.array([4,5,6])
print(c+d)
print(c*d)
space()
e=[1,2,3]
f=[4,5,6]
print(e+f)

#np는 각 요소마다 계산 되는 반면 그냥 리스트는 리스트끼리 합쳐지고 *는 아예 안됨
space()
print(np.dot(c,d))
print(c.dot(d))
# c와 d를 행렬 곱하라는 의미 1차원일 때는 d를 자동으로 전치 시켜 행렬곱을 해줌
space()
a= np.array([[1,2,3],[4,5,6]])
print(a)
print('행렬 크기',a.shape)
#[[],[]]로 감싸 np.array함으로써 2행3열 벡터를 만들었다
print(a[0,0])
print(a[1,1])
#a의 0행 0열 ,1행 1열 의 성분 출력 파이썬은 시작을 0부터 함
space()
b=np.array([[3,2,1],[6,5,4]])
print(b)
print('더하기')
print(a+b)
print('곱하기')
print(a*b)
# 각 성분끼리 더하고 곱한다
space()
b=([[1,2],[3,4],[1,2]])
print(np.dot(a,b))
#행렬 곱을 하기 위해서는 a 열과 b의 행의 갯수가 같아야한다
b=np.transpose(b)
print(b)
#b의 행과 열을 바꿔 주세요
space()
id =np.eye(3)
print(id)
#크기가 3인 단위 행렬을 출력해주셈
space()
b=np.array([[1,2],[3,4]])
b=np.linalg.inv(b)
print(b)
#가역인 경우 역함수를 구해주셈
space()
zero=np.zeros((3,5))
print(zero)
#3x5짜리 0행렬을 만들어 주세요
space()
one=np.ones((3,3))
print(one)
#3X3짜리 1행렬을 만들어 주세요
space()
full=np.full((3,3),7)
print(full)
#3x3 짜리 7행렬을 만들어 주세요, 7자리에 다른 숫자 넣어도 가능
space()
print('평균',np.mean(a))
print('표준편차', np.std(a))
print('중앙값',np.median(a))
print('최솟값',np.min(a))
print('최댓값',np.max(a))
