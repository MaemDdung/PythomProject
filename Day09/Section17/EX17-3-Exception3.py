'''
예외(Exception) 
    프로그램 존재하는 오류와 비슷하지만
    개발자가 직접 처리 할 수 있는 문제를 예외라한다.
    
ZeroDivisionError
ValueError
'''
try:
    a = int(input('제수를 입력하세요 >>> '))
    b = int(input('피제수를 입력하세요 >>> '))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print("0으 나눌 수 없습니다.")

except ValueError:
    print("정수만 입력 할 수 있습니다.")
except:
    print("예외가 발생했습니다")

