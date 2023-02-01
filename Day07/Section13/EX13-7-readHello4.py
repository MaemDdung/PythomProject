'''

readline()
    파일에서 1줄을 일고 그 결과를 리턴

'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    print(line_list)
    for line in line_list:
        print(line, end='')
