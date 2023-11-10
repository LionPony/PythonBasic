# 두 수의 연산값 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181938
def solution(a, b):
    num1 = int(str(a)+str(b))
    num2 = 2*a*b
    return num1 if num1 > num2 else num2