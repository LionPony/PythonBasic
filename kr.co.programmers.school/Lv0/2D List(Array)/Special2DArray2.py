# 특별한 이차원 배열 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181831
def solution(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr), 1):
            if arr[i][j] != arr[j][i] :
                return 0
    return 1