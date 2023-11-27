# 배열의 원소만큼 추가하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181861
def solution(arr):
    answer = []
    for i in arr :
        for j in range(i):
            answer.append(i)
    return answer