import matplotlib.pyplot as plt
def space():
    print()
    print()
x=[1,2,3,2,3,4]
plt.plot(x)
plt.show()
# plot(x):x의 값을 그래프로 표현 하라
# show() 보여줘
x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[]
for i in x:
    y.append(i**2)
plt.plot(x,y)
plt.show()
# plot(a,b)하면 a는 x축 b는 y축을 형성한다
plt.plot(x,y, marker='X')
plt.show()
#marker를 x로 표시
plt.plot(x,y, marker='X', linestyle='None')
plt.show()
# linestyle =None
plt.plot(x,y, linestyle='--')
plt.show()
# linestyle=--
