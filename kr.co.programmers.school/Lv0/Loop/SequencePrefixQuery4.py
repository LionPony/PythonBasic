# 수열과 구간 쿼리4
# https://school.programmers.co.kr/learn/courses/30/lessons/181923
import copy

def solution(arr, queries) :
    answer = copy.deepcopy(arr)
    for s, e, k in queries :
        for i in range(s, e+1) :
            try :
                if i % k == 0 :
                    answer[i] = answer[i] + 1
            except :
                # There are no multiples of 0
                pass
    return answer