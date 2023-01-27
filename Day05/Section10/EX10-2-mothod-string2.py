#join() 메소드
s = '_'.join('Python')
print(s)

s = '+'.join(["a", "b", "c", "d", "e"])
print(s)

s = ''.join(["a", "b", "c", "d", "e"])
print(s)

#split() 메소드
s = 'Life is to short'
result = s.split()
print(result)


s = '010-1234-4567'
result = s.split('-')
print(result)

data = '윤종훈|24|백수'
result = data.split('|')
print(result)
print('이름 :{}'.format(result[0]))

#replace() 메소드
s = 'Life is to short'
result = s.replace('short', "long")
print(result)

# strip, lstrip, rstrip 공백 제거
s = '       apple'
print(s)
result = s.lstrip() #왼쪽 공백 제거
print(result)

s = 'apple       '
result = s.rstrip() #오른쪽 공백 제거
print(result)

s = '       apple       '
result = s.strip() #양쪽 공백 제거
print(result)

s = ' a p p l e '
result = s.strip()  # 양끝 공백만 제거됨
print(result)
result = s.replace(' ', '') #전체 공백 제거
print(result)
