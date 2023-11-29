# 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
def solution(arr):
    goal = 1
    while(goal < len(arr)):
        goal *= 2
    for i in range(goal-len(arr)):
        arr.append(0)
    return arr