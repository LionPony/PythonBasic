# 수열과 구간 쿼리 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181883
def solution(arr, queries):
    for s, e in queries :
        for i in range(s, e+1) :
            arr[i] += 1
    return arr