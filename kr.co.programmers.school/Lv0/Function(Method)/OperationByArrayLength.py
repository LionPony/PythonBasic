# 배열의 길이에 따라 다른 연산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181854
def solution(arr, n):
    if len(arr)%2 == 1:
        for i in range(0, len(arr), 2):
            arr[i] = arr[i] + n
    else :
        for i in range(1, len(arr), 2):
            arr[i] = arr[i] + n
    return arr