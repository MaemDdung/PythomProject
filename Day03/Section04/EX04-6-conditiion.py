'''


조건 연산자(삼향 연산자)
    참if 조건식 else 거짓
    조건식 결과에 따라 참 또는 거짓의 결과를 반환 한다.

'''


a = 20
b = 10

result = (a - b) if(a >= b) else (b - a)  # (조건이 참일 때 실행문) if(조건문) else (조건이 거짓일 때 실행문)
print('{}과 {}의 차이는 {}입니다.'.format(a,b,result))
