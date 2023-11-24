# 길이에 따른 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181879
def solution(num_list):
    if len(num_list) >= 11 :
        return sum(num_list)
    else :
        ans = 1
        for i in num_list :
            ans *= i
        return ans