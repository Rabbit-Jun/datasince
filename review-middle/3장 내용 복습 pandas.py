import pandas as pd #pandas를 pd로 부르자
def space():
    print()
    print()
data = pd. read_csv('scores.csv') #csv 파일을 읽어드려서 변수 data에 저장
print(data)
space()
print(data.loc[data['Kor']>=80]) #데이터프레임 이름.loc[(행 조건문)]
#data['Kor']은 data의 열이름에서 kor에 해당하는 열의 값
space()
print(data.loc[data['Kor']>=80,'Name'])
#데이터프레임.loc[ 행조건문, 열 이름] 조건에 해당하는 값 중 Name 열만 출력
space()
data.loc[data['Kor']>=80,'Eng']+=1 # 열에다가 1 추가 여기서는 'Eng'
print(data)
space()
groups=data.groupby('Gender')
#데이터프레임 이름.groupby('열 이름') 해당 열에서 분류하고 싶을 때 사용
for a,b in groups:
    print('성별:',a)
    print(b)
    print('-'*10)    
# 변수 a에는 구분자의 값 (groups에 담겨있는 Gender에는 female과 male)
# 변수 b에는 해당 구분자의 데이터프레임 이 들어가있다
space()
print(len(data))
#데이터프레임을 넣은 data의 크기
space()
print(data.iloc[2])
#왼쪽에는 해당 타이틀 값  우측에는 []번째 행의 값을 가로로 출력한다
space()

for i in range(len(data)):
    print(data.iloc[i])
#특정 행을 0~부터 ldata-1l까지 출력
space()

for i in range(len(data)):
    row=data.iloc[i]
    avg=(row['Kor']+row['Eng']+row['Math'])/3
    print(avg)
"""
평균값을 계산하기 위해 특정 행을 넣은 row에서 kor,Eng,Math를 빼서
더한 후 3으로 나눔
"""
avgList=[]
for i in range(len(data)):
    row=data.iloc[i]
    avg=(row['Kor']+row['Eng']+row['Math'])/3
    avgList.append(avg)
print(avgList)
print('-'*20)
data['Average']=avgList
print(data)
"""
빈 리스트avgList를 만든 후 평균 값을 계산한 avg를 avgList안에 넣어준다 그 후
data['Average']를 하여 Average를 만들어 준 후 avgList를 넣어준다
"""
data.to_csv('scores.csv')
#socres.csv에 data를 csv형태로 저장하라는 뜻

