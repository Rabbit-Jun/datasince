
# proble to chap 1-1
# 임의의 수를 입력받아 해당 숫자가 소수인지를 판별하는 프로그램을 작성하시오
user=int(input('값을 입력하세요:' ))
def proun(user):
    while True:
        prime=True
        for i in range(2,user):
            r =user%i
            if r ==0:
                prime=False
                break
        if prime:
            print('소수입니다')
        else:
            print('소수가 아닙니다')
        
        user=int(input('값을 입력하세요:' ))
        if user ==0:
            break
    
proun(user)
            
