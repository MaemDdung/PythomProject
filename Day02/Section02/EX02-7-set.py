'''
Set
    순서가 없다.
    변경할 수 없다.
    인덱싱 되지 않는 컬렉션
    중복값 없다.
'''
from builtins import print

thisset  = {"피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"}
#실행할 때 마다 순서가 변경됨
print(thisset)

#항목 가져오기
#반복문 사용
for x in thisset: #thisset 길이 만큼 반복 
    print(x)
    
#값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("피츄" in thisset)

#항목 추가하기
thisset.add("꼬부기")
print(thisset)


#다른 Set 항목 추가
thisset1  = {"피카츄", "라이츄", "꼬부기"}
thisset2  = {"파이리", "버터플", "야도란"}
thisset1.update(thisset2)
print(thisset1)

#항목 제거
thisset  = {"피카츄", "라이츄", "꼬부기"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄")#없는 항목 지우면 에러남
# print(thisset)

#discard는 없는 항목을 지워도 에러 없음
thisset  = {"피카츄", "라이츄", "꼬부기"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

thisset  = {"피카츄", "라이츄", "꼬부기"}
thisset.pop()
print(thisset)

#비우기
thisset  = {"피카츄", "라이츄", "꼬부기"}
thisset.clear()
print(thisset)