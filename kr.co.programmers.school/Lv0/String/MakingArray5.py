# 배열 만들기 5
# https://school.programmers.co.kr/learn/courses/30/lessons/181912
def solution(intStrs, k, s, l):
    answer = []
    temp = ""
    for i in intStrs :
        for j in range(s, s+l) :
            temp = temp + i[j]
        if int(temp) > k :
            answer.append(int(temp))
        temp = ""
    return answer