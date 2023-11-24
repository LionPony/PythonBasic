# 문자 개수 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/181902
from string import ascii_lowercase, ascii_uppercase
def solution(my_string):
    answer = {}
    for i in ascii_uppercase :
        answer[i] = 0
    for i in ascii_lowercase :
        answer[i] = 0
    
    for i in range(len(my_string)) :
        answer[my_string[i]] = answer[my_string[i]] + 1

    return list(answer.values())