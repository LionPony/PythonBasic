# 조건에 맞게 수열 변환하기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181835
def solution(arr, k):
    if k % 2 == 0:
        result = map(lambda x : x+k, arr)
    else :
        result = map(lambda x : x*k, arr)
    return list(result)