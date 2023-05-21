"""
numpy의 np.random.randint(n)은 0부터 n-1까지의 정수 중에서 임의의 숫자를
생성한다. 이 기능을 이용하여 다음 프로그램을 구현하시오

* 1번 주사위를 100번 던졌을 때 나타나는 주사위 눈의 값을 x에 저장
* 2번 주사위를 100번 던졌을 때 나타나는 주사위 눈의 값을 y에 저장
* 3번 주사위를 100번 던졌을 때 나타나는 주사위 눈의 값을 z에 저장
* x를 이용하여 주사위 하나를 던졌을 때의 주사위 눈의 최솟값, 최대값, 평균,
    표준편차를 계산
* x,y를 이용하여 주사위 두개를 던졌을 때의 주사위 눈 합계의 최솟값, 최대값, 평균,
    표준편차를 계산
* x,y,z를 이용하여 주사위 세개를 던졌을 때의 주사위 눈의 합계의 최솟값, 최대값, 평균,
    표준편차를 계산
"""
import numpy as np
x=[]
y=[]
z=[]
for _ in range(100):
    rx=np.random.randint(1,7)
    x.append(rx)
    ry=np.random.randint(1,7)
    y.append(ry)
    rz=np.random.randint(1,7)
    z.append(rz)
x=np.array(x)
y=np.array(y)
z=np.array(z)

print(f'x의 최솟값:{np.min(x)},최대값:{np.max(x)},평균:{np.mean(x)},표준편차:{np.std(x)}')
print(f'x+y의 최솟값:{np.min(x+y)},최대값:{np.max(x+y)},평균:{np.mean(x+y)},표준편차:{np.std(x+y)}')
print(f'x+y+z의 최솟값:{np.min(x+y+z)},최대값:{np.max(x+y+z)},평균:{np.mean(x+y+z)},표준편차:{np.std(x+y+z)}')
