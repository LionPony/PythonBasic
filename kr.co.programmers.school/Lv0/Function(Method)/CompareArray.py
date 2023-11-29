# 배열 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181856
def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else :
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else :
            return 0