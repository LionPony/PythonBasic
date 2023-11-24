# 왼쪽 오른쪽
# https://school.programmers.co.kr/learn/courses/30/lessons/181890
def solution(str_list):
    for i in range(len(str_list)) :
        if str_list[i] == 'l' :
            return str_list[:i]
        elif str_list[i] == 'r' :
            return str_list[i+1:]
    return []