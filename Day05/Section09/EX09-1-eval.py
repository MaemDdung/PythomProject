'''
eval() 함수
    매개 변수로 받은 expression(=식)을
    문자열로 받아서 실행하는 함수
'''
expr = input("계산식을 입력하세요 >>> ")     # 문자열로 받는다
result = eval(expr)                       # 수식으로 받아서 반환
print(expr + "=" + str(result))