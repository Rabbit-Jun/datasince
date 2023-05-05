"""
임의의 연도가 윤년인지를 판별하는 함수를 작성하고,
이 함수를 이용하여 임의의 연도를 입력받아 해당 연도가 윤연인지 평년인지
출력하는 프로그램을 작성하시오
"""
#윤년 내 대답
def discern (year):
    while True:
        if year%4==0 and year%100!=0 or year%4==0 and year%100==0 and year%400==0:
            print(f"{year}는 윤년")
            
        else:
            print(f"{year}윤년이 아니다")
        year=int(input("input the year:"))
        if year ==0:
            break
        
year=int(input("input the year:"))
discern(year)
#윤년 책 대답

def check leap(x):
    if x%4 ==0:
        if x%100 ==0:
            if x%400 ==0:
                y=1
            else:
                y=0
        else:
            y=1
    else:
        y=0
    return y
x=int(input("연도를 입력하세요:")
leap=check_leap(x)
print(leap)
if leap==1:
      print("유년 입니다")
else:
    print("평년 입니다")
    
