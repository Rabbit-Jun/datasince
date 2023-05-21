"""
1-2 문제
임의의 연도가 윤년인지를 판별하는 함수를 작성하고, 이 함수를 이용하여 임의의
연도를 입력받아 해당 연도가 윤년인지 평년인지 출력하는 프로그램을 작성하시오
4로 나누어떨이지거나 400으로 나누어 떨어지는 경우
"""
year=int(input('년도를 입력하세요: '))
def proun(year):
    while True:
        if (year%4 ==0 and year%100 ==0 and year%400 ==0 )or (year%4 ==0 and year%100 !=0):
            print('윤년')
        else:
            print('평년')
        year=int(input('년도를 입력하세요: '))
        if year==0:break

proun(year)
