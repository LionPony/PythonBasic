# 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix :
        return 1
    return 0