# 수열과 구간 쿼리3
# https://school.programmers.co.kr/learn/courses/30/lessons/181924
import copy
def solution(arr, queries):
    answer = copy.deepcopy(arr)
    for query in queries:
        swap(answer, query[0], query[1])
    return answer

def swap(arr, i, j) :
    arr[i], arr[j] = arr[j], arr[i]