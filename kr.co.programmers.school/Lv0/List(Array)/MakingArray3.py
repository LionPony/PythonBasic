# 배열 만들기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181895
def solution(arr, intervals):
    answer = []
    for a, b in intervals :
        answer += arr[a:b+1]
    return answer