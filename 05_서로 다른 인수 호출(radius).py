################ 서로 다른 인수 호출 코딩
################ 파이썬은 인터프리터 언어이기 때문에 함수의 순서가 매우 중요

def get_area(radius):
    area = 3.14 * radius**2
    return area

result1 = get_area(3)
result2 = get_area(20)

print("반지름이 3인 원의 면적=", result1)
print("반지름이 20인 원의 면적=", result2)
