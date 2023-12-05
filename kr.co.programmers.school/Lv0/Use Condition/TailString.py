# 꼬리 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181841
def solution(str_list, ex):
    answer = []
    for i in str_list:
        if ex not in i:
            answer.append(i)
    return "".join(answer)