################ 팩토리얼 계산
################ 파이썬은 인터프리터 언어이기 때문에 함수의 순서가 매우 중요

import numpy as np

def factorial(n):
    if n == 1 :
        return(1)
    else:
        return n * factorial(n-1)
    
n = eval(input("정수를 입력하시오:"))
print(n, "!= ", factorial(n))
