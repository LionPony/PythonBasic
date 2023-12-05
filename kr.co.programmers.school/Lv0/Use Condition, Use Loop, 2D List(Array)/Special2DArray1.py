# 특별한 이차원 배열 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181833
def solution(n):
    answer = []
    for i in range(n):
        element = []
        for j in range(n):
            if i == j:
                element.append(1)
            else :
                element.append(0)
        answer.append(element)
    return answer