'''
파일 복사
    원본 -> 버버 편수(memory) -> 복사본


'''

buffer_size = 1024  #1024byte -> 1KB의미

with open('../../Day07/Section13/hello.txt', 'rb') as source:
    with open('hello2.txt','wb') as copy:
        while 1:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print("hello2.txt파일이 복사되었습니다.")







