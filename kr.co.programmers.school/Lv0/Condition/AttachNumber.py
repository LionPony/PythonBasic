# 이어 붙인 수
# https://school.programmers.co.kr/learn/courses/30/lessons/181928
def solution(num_list):
    evens = ''
    odds = ''
    for i in num_list :
        if i%2 == 0 :
            evens += str(i)
        else :
            odds += str(i)
    return int(evens) + int(odds)