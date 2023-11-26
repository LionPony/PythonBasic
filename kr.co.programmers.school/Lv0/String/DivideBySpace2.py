# 공백으로 구분하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181868
def solution(my_string):
    my_string.sub('\s+', ' ')
    return my_string.strip().split(' ')

def solution2(my_string):
    return my_string.split()