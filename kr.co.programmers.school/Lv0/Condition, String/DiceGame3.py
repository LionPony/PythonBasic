# 주사위 게임 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181916
def solution(a, b, c, d):
    sameMap = dict()
    parameter = [a, b, c, d]
    for i in parameter :
        if i in sameMap :
            sameMap[i] = sameMap[i] + 1
        else :
            sameMap[i] = 1

    score = 0
    case = len(parameter) - len(sameMap)

    if case == 3 :
        for key in sameMap.keys() :
            score = 1111 * key
    elif case == 2 :
        p = 0
        q = 0
        if 3 in sameMap.values() :
            for key in sameMap.keys() :
                if sameMap[key] == 3 :
                    p = key
                elif sameMap[key] == 1 :
                    q = key
                score = (10 * p + q)**2
        elif 2 in sameMap.values() :
            keys = []
            keys = list(sameMap.keys())
            p = keys[0]
            q = keys[1]
            score = (p + q) * abs(p - q)
    elif case == 1 :
        score = 1
        for key in sameMap.keys() :
                if sameMap[key] == 1 :
                    score *= key
    elif case == 0 :
        score = min(sameMap.keys())
    return score