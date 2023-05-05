"""
구구단을 3개씩의 단이 병렬적으로 동시에 나타나도록 하고,
단의 끝에 구분선이 표시되도록 하시오.
"""
l='-'*7
for i in range(2,10,3):
    for  n in range(1,10):        
        def ca(x,y):
            x=f'{x}*{y}={x*y}'          
            return f'{x:^7}'
        if i<8:
            print(ca(i,n),ca(i+1,n),ca(i+2,n))
        else:
            print(ca(i,n),ca(i+1,n))
        if i<=5 and n ==9:
            print(l,l,l,sep=' ')
        elif i==8 and n==9:
            print(l,l,sep =' ')

 
    

