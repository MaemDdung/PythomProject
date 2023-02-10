'''
예외(Exception) 
    프로그램 존재하는 오류 비슷하지만
    개발자가 직접 처리 할 수 있는 문제를 예외라한다.
    

코드 작성 방법
try:
    코드 작성 영역 (정상코드)

except:
    예외 발생시 처리 영역
'''
try:
    a = int(input('제수를 입력하세요 >>> '))
    b = int(input('피제수를 입력하세요 >>> '))
    print('{} / {} = {}'.format(a, b, a / b))

except:
    print("예외가 발생했습니다")

