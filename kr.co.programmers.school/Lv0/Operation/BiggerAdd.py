# 더 크게 합치기
# https://school.programmers.co.kr/learn/courses/30/lessons/181939
def solution(a, b):
    num1 = int(str(b) + str(a))
    num2 = int(str(a) + str(b))
    return num1 if num1 > num2 else num2