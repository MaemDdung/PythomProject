'''
open함수 모드 
    w(wrote mode) : 파일 없으면 생성
    t(text mode) : 해당 파일의 데이터를 텍스트 파일로 인식하고 입출력
    b(binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력
    a(append mode) : 해당 파일의 데이터를 추가 한다
    r(read mode) : 읽기 전용 모드/ 파일 없에면 에러

경로
    절대 경로 예) C:\pstudy\PythomProject\Day07\Section13\hello.txt
    상대 경로 예) ./upload/hello2.txt
             예) ../../폴더명 파일
            .  -> 현재폴더
             .. -> 상위폴더
            (윈도우os) 최상위 경로 (root) / 또는  c:/
'''


file = open('hello.txt', "wt", encoding='UTF-8' )
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성 되었습니다.')
file.close()


# file = open('hello2.txt', "wt", encoding='utf-8')
# file.write('2안녕하세요\n')
# file.write('2반갑습니다\n')
# print('hello2.txt 파일이 생성 되었습니다.')
# file.close()