# 배열 만들기 6
# https://school.programmers.co.kr/learn/courses/30/lessons/181859
def solution(arr):
    i = 0
    stk = []
    while(i < len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
            continue
        lastElement = stk[-1]
        if lastElement == arr[i] :
            stk.pop()
        else :
            stk.append(arr[i])
        i += 1
    return stk if len(stk) >= 1 else [-1]