# 마지막 두 원소
# https://school.programmers.co.kr/learn/courses/30/lessons/181927
import copy
def solution(num_list):
    answer = copy.deepcopy(num_list)
    beforeLast = num_list[-2]
    last = num_list[-1]
    if last > beforeLast :
        answer.append(last-beforeLast)
    else :
        answer.append(last*2)
    return answer