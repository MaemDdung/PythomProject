'''
주말 숙제

[회원 가입]
아이디를 입력하세요 (3글자 이상) >>>
> 3글자 이상 입력해 주세요!

아이디를 입력하세요(3글자 이상) >>>

패스워드를 입력하세요(영문 숫자 포함 8자이상 >>>
>영문 숫자 포함 8자 이상 입력해주세요!


패스워드를 확인 한번더 입력하세요 >>>
>일치 하지 않습니다! 다시입력해주세요!

패쓰워드를 입력하세요(영문 숫자 포함 8자이상 >>>


패쓰 워드 확인 한번 더 입력하세요 >>>
회원 가입 완료

[로그인]
아이드를 입력하세요 >>>
> 아이디가 일치하지 않습니다

패쓰워드를 입력하세요 >>>
>패쓰워드가 일치하지 않습니다.

패쓰워드를 입력하세요 >>>

로그인 성공!
(아이디값)  환영합니다
'''
#미완성

while 1:

    id = list(input("아이디를 입력하세요 (3글자 이상) >>>"))

    if len(id) >= 3: 
        print("아이디 입력 완료")
        break
            

    else:
        print("> 3글자 이상 입력해 주세요!")
        continue


while 1:
    pw = list(input("패스워드를 입력하세요(영문 숫자 포함 8자이상 >>>"))
    isContainAlpha = False
    isContainNumeric = False

    if len(pw) >= 3:    #유효성 검사 못함 우쨰하누..
        for ch in pw:
            if ch.isalpha():
                isContainAlpha = True
            elif ch.isContainNumeric():
                isContainNumeric = True

        pw2 = list(input("패쓰 워드 확인 한번 더 입력하세요 >>>"))
        if pw == pw2:
            print("회원가입 완료")
            break
        else:
            print("> 패스워드가 일치하지 않습니다.")
            continue
        
            

    else:
        print("> 영문 숫자 포함 8자 이상 입력해주세요!")
        continue


while 1:
    user_id = list(input("아이드를 입력하세요 >>>"))
    if user_id == id:
        user_pw = list(input("패스워드를 입력하세요 >>>"))
        if user_pw == pw2:
            print(*id, "님 환영합니다.")
            break
        else:   
            print("> 패스워드가 일치하지 않습니다.")
            continue
    else:
        print("> 아이디가 일치하지 않습니다.")
        continue       

