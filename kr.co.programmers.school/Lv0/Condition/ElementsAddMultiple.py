# 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
def solution(num_list):
    multiple = 1
    add = 0
    for i in num_list :
        multiple = multiple * i
        add = add + i
    return 1 if add**2 > multiple else 0