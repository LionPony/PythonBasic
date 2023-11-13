# 주사위 게임 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181930
def solution(a, b, c):
    score = 0
    same = 0
    
    if a == b :
        same += 1
    if a == c :
        same += 1
    if b == c :
        same += 1

    if same == 0 :
        score = a + b + c
    elif same == 1 :
        score = (a + b + c) * (a**2 + b**2 + c**2)
    else :
        score = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

    return score