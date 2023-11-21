# 세로 읽기
# https://school.programmers.co.kr/learn/courses/30/lessons/181904
def solution(my_string, m, c):
    answer = my_string[c-1::m]
    return answer