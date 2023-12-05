# 커피 심부름
# https://school.programmers.co.kr/learn/courses/30/lessons/181837
def solution(order):
    americanoCount = 0
    latteCount = 0
    for i in order:
        if "latte" in i:
            latteCount += 1
        else :
            americanoCount += 1
    return 4500 * americanoCount + 5000 * latteCount