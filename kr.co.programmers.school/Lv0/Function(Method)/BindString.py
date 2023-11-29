# 문자열 묶기
# https://school.programmers.co.kr/learn/courses/30/lessons/181855
def solution(strArr):
    map = dict()
    for i in strArr:
        if len(i) not in map:
            map[len(i)] = 1
        else :
            map[len(i)] = map[len(i)] + 1
    return max(map.values())