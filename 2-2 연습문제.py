"""
다음의 오일러의 공식으로 원주율을 계산하는 프로그램을 작성하시오
"""
import math
sum=0
for n in range(1,1000000):    
    sum+=1/(n**2)
pi_squared=6*sum
pi=math.sqrt(pi_squared)
print(pi)
    
   



