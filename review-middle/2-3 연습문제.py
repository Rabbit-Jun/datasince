"""
임의의 문자열을 넘겨주면 그 문자열을 역순으로 리턴하는 함수를 만들고,
이 함수를 이용하여 임의의 문자열이 화문인지를 판별하는 프로그램을 작성하시오.
단, 공백은 무시하시오.
(회문은 거꾸로 읽어도 바로 읽어도 똑같은 것 ex.우영우,토마토,기러기,스위스)

"""
while True:
    str_judge=input("회문 판독기:")
    if str_judge=='0':
        break
    def string_reverse(str):
        re_str=''
        for i in str:
            re_str=i+re_str
            
        print(re_str)
        if str==re_str:
            print("회문입니다")
        else:
            print("회문이 아닙니다")
    string_reverse(str_judge)
   
    
