'''

Dictionary
    key:value 로 이루어져 쌍으로 데이터 값을 저장하는데 사용

'''


#ductionary 선언
thisdict = {
    "brand":"나이키",
    "model":"max90",
    "year":1990
}
print(thisdict)

'''
키 이름을 사용하여 참조 할 수 있다.
'''
#값 가져오기
thisdict = {
    "brand":"나이키",
    "model":"max90",
    "year":1990
}
print(thisdict["brand"])
print(thisdict.get("model"))

# 키 목록 가져오기
print(thisdict.keys())

#cnrk gkrl
thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "red"
print(thisdict)

thisdict.update({"bgColor":"black"})
print(thisdict)


#변경하기
thisdict["color"] = "yellow"
thisdict.update({"bgColor":"blue"})
print(thisdict)

#제거하기
thisdict.pop("model")
print(thisdict)

#마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)