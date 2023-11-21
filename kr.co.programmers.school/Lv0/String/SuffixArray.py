# 접미사 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/181909
def solution(my_string):
    answer = []
    for i in range(len(my_string)) :
        answer.append(my_string[i:])
    answer.sort()
    return answer