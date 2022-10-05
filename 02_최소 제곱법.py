#파이썬 코딩으로 확인하는 최소 제곱
#오차를 최소화 시키는 방법으로 회귀 계수
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# y = ax + b 으로 일차 함수 그래프를 표시 가능


import numpy as np; #파이썬에서 수학을 가능하게 해주는 라이브러리

x = np.array([2, 4, 6, 8]); #공부한 시간에 따른
y = np.array([81, 93, 91, 97]); #시험 점수 결과

mx = np.mean(x); #공부시간 평균 계산
my = np.mean(y); #성적의 평균 계산

print("x의 평균값:", mx); #공부한 시간의 평균 표출
print("y의 평균값:", my); #성적의 평균 값 표출

# 최소 제곱법 기울기 공식의 분모 부분
divisor = sum([(i-mx)**2 for i in x]) #**2 2제곱을 구하라는 말

# 최소 제곱법 기울기 공식의 분자 부분입니다.
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, mx, y, my)

# 출력으로 확인합니다.
print("분모:", divisor)
print("분자:", dividend)

# 기울기 a를 구하는 공식입니다.
a = dividend / divisor  #2.3 #46/20

# y절편 b 를 구하는 공식입니다.
b = my - (mx*a)

# 출력으로 확인합니다.
print("기울기 a =", a)
print("y절편 b =", b)

#끝


