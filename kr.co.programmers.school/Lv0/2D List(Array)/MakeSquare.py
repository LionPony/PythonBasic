# 정사각형으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181830
def solution(arr):
    low = len(arr)
    col = 1
    for i in arr:
        if len(i) > col:
            col = len(i)
    if col < low:
        for i in arr:
            for j in range(low-col):
                i.append(0)
    elif low < col:
        for j in range(col - low):
            arr.append([0 for i in range(col)])
    return arr