# 부분 문자열인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181843
def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0