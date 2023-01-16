'''
List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''

thislist = ["피카츄", "라이츄", "파이리"]
print(thislist)
print(thislist[0])
print(thislist[0][0])   #"피카츄"[0]

#List길이
print(len(thislist))

list1 = ["피카츄", "라이츄", "파이리"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, False]
#다양한 유형 포함가능
list4 = ["abc", 30, False, 20]

#항목접근
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist[1])

#변경
thislist[1] = "잠만보"
print(thislist)


#힝목변경 2개
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
print(thislist)
thislist[1:3] = ["울먹이", "메타몽"] #인덱스 1번 2번 값 변경
print(thislist)

#두번째 세번째 값을 하나의 값으로 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)

#항목추가
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist)
thislist.append("꼬부기")
print(thislist)

#항목추가 - 인덱스 번호로 추가
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist)
thislist.insert(1, "잠맘보")
print(thislist)

#항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist)
thislist.remove("라이츄")
print(thislist)

#항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist)
thislist.pop(2)
print(thislist)

#마지막 값 제거
thislist = ["피카츄", "라이츄", "파이리", "잠만보"]
print(thislist)
thislist.pop() #값을 안넣으면 마지막값 제거 된다
print(thislist)

#목록 삭제 리스트 겁데기만 남는다 (값만 삭제)
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist)
thislist.clear()
print(thislist)

#확장
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터플", "야도란"])
print(thislist)

#리스트 객체 자체를 삭제 / NameError: name 'thislist' is not defined
# del thislist
# print(thislist)

