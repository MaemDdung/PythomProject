'''
for 문
    값의 범위나 횟수가 정해져 있을때 사용하면 편리한 반복문
    while문 보다 자주 사용된다
    
for 변수 in 반복 가능한 객체:
    반복문 실행
    
'''

pwd = input("비밀번호를 입력하세요.>>> ")

ch_count = 0
num_count = 0
for ch in pwd:              #문자의 배열 (인덱스)
    if ch.isalpha():        #메소드 문자여부 bool타입으로 반환
        ch_count += 1
    elif ch.isnumeric():    #메소드 숫자여부 bool타입으로 반환
        num_count += 1
      
if ch_count > 0 and num_count > 0:
    print("가능한 비밀번호 입니다.")
else: 
    print("불가능한 비밀번호 입니다.")
