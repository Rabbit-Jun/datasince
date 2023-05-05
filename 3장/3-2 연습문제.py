"""
scores.csv의 내용을 데이터프레임으로 읽어들이고, 각 학생의 평균점수에 따라
학점을 부여하여 새로운 열로 추가하시오.
(단, 학점은 70점 이상은 C, 75점 이상은  C+,80점 이상은 B, 85점 이상은 B+,
90점 이상은 A, 95점 이상은 A+임)
"""
import pandas as pd
data=pd.read_csv('scores.csv')

data.loc[data['Average']>=95,'Grade']='A+'
data.loc[data['Average']<95,'Grade']='A'
data.loc[data['Average']<90,'Grade']='B+'
data.loc[data['Average']<85,'Grade']='B'
data.loc[data['Average']<80,'Grade']='c+'
data.loc[data['Average']<75,'Grade']='c'
data.loc[data['Average']<70,'Grade']='null'

    
print(data)
