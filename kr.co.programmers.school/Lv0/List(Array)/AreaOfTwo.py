# 2의 영역
# https://school.programmers.co.kr/learn/courses/30/lessons/181894
def solution(arr):
    start = -1
    end = -1

    for i in range(len(arr)) :
        if arr[i] == 2 :
            start = i
            break

    for i in range(len(arr)-1, -1, -1) :
        if arr[i] == 2 :
            end = i
            break

    return arr[start:end+1] if start != -1 else [-1]