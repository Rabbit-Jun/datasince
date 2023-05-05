"""
파이썬의 자료구조 중에는 딕셔너리가 있다.
딕셔너리 자료구조를 활용하여 전화번호부 프로그램을 작성하시오.
10명 이산의 연락처를 저장해두고 이름을 입력하면 전화번호가 출력되도록 하시오
"""
while True:
    def phone_book(name):
        phone_num={'a':112,'b':222,'c':369,'d':42,'e':51,'f':62,'g':755,'h':83,'i':119,'j':100}
        print(phone_num[name])
    name=input("어떤 사람의 전화번호를 찾아드릴까요? :")
    if name =='0':
        break

    phone_book(name)
    
