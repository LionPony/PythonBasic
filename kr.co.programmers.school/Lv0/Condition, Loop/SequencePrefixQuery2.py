# 수열과 구간 쿼리2
# https://school.programmers.co.kr/learn/courses/30/lessons/181923
def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        part = []
        for i in arr[s:e+1] :
            if i > k :
                part.append(i)
        if len(part) == 0 :
                answer.append(-1)
        else :
            answer.append(min(part))
    return answer