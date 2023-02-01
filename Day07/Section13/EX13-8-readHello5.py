'''

readline()
    파일에서 1줄을 일고 그 결과를 리턴

'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    for no, line in enumerate(line_list):
        print('{} {}'.format(no+1, line), end="")
