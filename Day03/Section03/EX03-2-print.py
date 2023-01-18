'''
print() 함수 사용법
    sep : 출력할 value의 구분 문자
    end : value 출력 후 출력할 문자 (기본값 '\n')
    file : 출력 방향 지정
'''

print("재미있는","파이썬") #sep값이 안보이지만 들어 갔다.
print('python', "JAVA", 'C', sep=" ")
print("안녕", end="") #기본이  end="\n"이지만 지워줌으로 이어서 나옴
print("하세요")

fos = open('sample.py', mode='wt')      #sample.py를 만들겠다 w 쓰겠다 t 텍스트를
print('print("Hello World")',file=fos)  #print("Hello World") 쓰겠다 
fos.close()