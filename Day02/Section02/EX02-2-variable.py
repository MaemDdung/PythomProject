'''
변수(variable)
    어떤 데이터를 저장하고 할 때 사용하는 메모리 저장소
    
변수명 규칙
    영문, 한글, 숫자, 밑줄로(_) 구성된다.
    특수문자(!@#$%^&*()_+ 등) 사용할 수 없다!!
    대문자 소문자를 구분한다
    변수명의 첫글자를 숫자로 사용할 수 없없다
    키원드 (list, dict, if, for, and, or, 등)은 사용 할 수 없다!!!
    
'''
#변수명 = 값



name = "Alice"
print(name)

age = 25
print(age)


#몰랐던거
addresds = '''우편번호 12345
서울시 강서구 방화동 123-45
'''
print(addresds)


# 잘못된 변수명
# 2mybay = "python1"
# my-bay = "python2"
# my bay = "python3"
# $mybay = "python4"

'''
여러 값 할 당
   Python을 사용하면 한줄에 여러 변수에 값을 할 당 할 수 있다
tip) ctrl + D 줄복사   
'''
x, y, z = "피카츄", "라이츄", "파이리"
print(x)
print(y)
print(z)

x = y = z = "꼬부기"
print(x)
print(y)
print(z)
