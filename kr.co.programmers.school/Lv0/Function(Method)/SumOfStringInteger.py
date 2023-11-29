# 문자열 정수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181849
def solution(num_str):
    result = 0
    for i in range(len(num_str)):
        result += int(num_str[i])
    return result