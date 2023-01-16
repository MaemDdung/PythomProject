'''
Docstring 보여주려는 예제 ㅋㅋㅋ!


'''


#math모율 포함
import math

#get_area()함수 정의
def get_area(radius):
    """\"반지름을 입력 받아서 원의 넗이를 반환 하는 get_area() 함수\""""#Docstring 
    area = math.pi * math.pow(radius, 2)
    return area

radius = 1.5 #반지름
print(radius)

#get_area() 함수 호출 결과를 area변수에 저장
area = get_area(radius)
print("%f"% area)
print(get_area.__doc__) # Docstring 확인