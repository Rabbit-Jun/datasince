import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b=pd.read_csv('buylov.csv')
plt.scatter(b['BGiftPrice'],b['Apprec-7'])
plt.show()
# 산점도를 이용해 BGiftPrice와 Apperec-7의 관계를 시각화
bg=b[b['Role']=='Giver']
br=b[b['Role']=='Receiver']
plt.figure('giver')
plt.scatter(bg['BGiftPrice'],bg['Apprec-7'])
plt.figure('reciever')
plt.scatter(br['BGiftPrice'],br['Apprec-7'])
plt.show()
# figure을 통해 산점도 구분
