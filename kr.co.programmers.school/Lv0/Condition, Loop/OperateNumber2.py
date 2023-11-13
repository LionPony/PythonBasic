# 수 조작하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181925
def solution(numLog):
    scan = numLog[0]
    answer = ""
    for log in numLog[1:] :
        diff = log-scan
        if diff == -1 :
            answer = answer + "s"
        elif diff == -10 :
            answer = answer + "a"
        elif diff == 1 :
            answer = answer + "w"
        elif diff == 10 :
            answer = answer + "d"
        scan = log
    return answer