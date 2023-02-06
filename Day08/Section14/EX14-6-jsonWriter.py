'''

JSON (JavaScript Object Notation)
    - 딕셔너리 비슷하다
    - 구조 { k : V }
'''



import json



'''
#첫번째 방법
dict_list=[
    {
        'neme': 'james',
        'age': 20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'neme': 'alice',
        'age': 21,
        'spec':[
            168.5,
            60.5
        ]
    }

]

json_string = json.dumps(dict_list)

with open('dictList.json','w') as file:
    file.write(json_string)
print("dictList.json 파일이 생성 되었습니다.")
'''

#두번째 방법
dict_list=[
    {
        'name': '김철수',
        'age': 20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name': '홍길동',
        'age': 21,
        'spec':[
            168.5,
            60.5
        ]
    }

]
# indent 들여쓰기, ensure_ascii=False 한글읽기
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)

with open('dictList.json', 'w', encoding='UTF-8') as  file:
    file.write(json_string)
print("dictList.json파일이 생성 되었습니다")



