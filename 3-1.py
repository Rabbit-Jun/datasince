"""
'scores.csv'데이터 파일을 이용하여 특정 학생의 특정 과목 점수에 보너스 점수를
부여하는 프로그램을 작성하시오. 변경 전 성적 리스트를 보여주고,
학생의 이름 및 과목명을 입력받으면 해당 과목 점수를 보여준 후, 부여할 보너스
점수를 입력받아 이를 해당 과목 점수에 더하고 변경된 성적 리스트를 출력하도록
하시오
"""
import pandas as pd
data=pd.read_csv('scores.csv')


print("학생의 데이터")
print(data)

    
    
           
                
                
def score():
        spell= False
        while True:
            print("종료를 원하시면 학생의 이름에 0을 입력해주세요")
            
    
            while True:
                name=input("찾으시는 학생의 이름을 입력해주세요:")
                if name =='0':
                    break
                name=name.capitalize()
            
                for i in data['Name']:
                    if name ==i:
                        print(data.loc[data['Name']==name])
                        spell=True
                        break
                if spell ==False:
                    print("잘못 입력하셨습니다")
                    break
                while True:
                    
                    subject=input("어떤 과목의 점수를 수정할지 입력해주세요:")
                    subject=subject.capitalize()
                    for i in ['Kor','Eng','Math']:
                       
                        if subject==i:
                            spell=True
                            break
                        elif subject !=i:
                            
                            spell= False
                        
                        
                            
                            
                    if spell ==True:
                        
                        break
                    print("잘못 입력하셨습니다")

                
                bonus=input("몇점을 추가하시겠습니까?:")
                bonus=int(''.join(filter(str.isdigit,bonus)))
                data.loc[data['Name']==name,subject]+=bonus
                print(data)
            if name =='0':
                print("프로그램을 종료합니다")
                break
    
score()


