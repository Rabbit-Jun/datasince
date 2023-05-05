"""
scores.csv의 내용을 x라는 이름의 데이터프레임으로 읽어들여서,
Betty의 수학 점수를 90점으로 수정해야 한다.이 때, 다음 여섯 가지 방식 중
옳은 방법과 작동되지 않는 방법을 구분하고, 어떤 차이가 있는지를 설명하시오
1 x[x['Name']=='Betty']['Math']=90
2 x.loc[x['Name']=='Betty']['Math']=90
3 x.loc[x['Name']=='Betty','Math']=90
4 x.iloc[1]['Math']=90
5 x.iloc[1,'Math']=90
6 x.iloc[1,5]=90
"""
#3,6 번이 정상적인 방법이고 나머지 방법은 데이터를 읽을 수는 있지만 사본을 반환함
