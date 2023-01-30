'''
지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용 가능

전역 변수(global)
    함수 외부 선언
    함수 내부 외부 모두 사용 가능

'''

gVar = '전역'
def globaAndLocal ():
    lVar = '지역'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globaAndLocal()

gVar = '전역'
def globaAndLocal2():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globaAndLocal2()




#전역변수 선언
total = 0 
def gift(dic,who,money):
    global total
    total += money
    dic[who] = money

wedding={}
gift(wedding, '영희', 5)
gift(wedding, '철수', 6)
gift(wedding, '이모', 10)

print('축의금 명단: {}'.format(wedding))
print('축의금 명단: {}'.format(total))