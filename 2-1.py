#2-1 실습 예제
#임의이 수를 입력받아 해당 숫자가 소수인지를 판별하는 프로그램을 작성하시오.
while True:   
    prime=True
    user=int(input('숫자를 입력하세요:'))
    for i in range(2,user):
        
        if user%i==0:
            
            prime=False
            break
    if prime :
        print(f"{user} is prime")
    else:
        print(f"{user} isn't prime")
        
    if user== 0:
        break
        
