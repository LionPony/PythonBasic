# 문자열의 뒤의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181910
def solution(my_string, n):
    return my_string[len(my_string)-n:len(my_string)]