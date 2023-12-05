# 주사위 게임 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181839
def solution(a, b):
    oddCount = 0
    if a % 2 == 1:
        oddCount += 1
    if b % 2 == 1:
        oddCount += 1

    if oddCount == 0:
        return abs(a-b)
    elif oddCount == 1:
        return 2 * (a + b)
    else:
        return a**2 + b**2