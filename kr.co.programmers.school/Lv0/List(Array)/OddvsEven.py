# 홀수 vs 짝수
# https://school.programmers.co.kr/learn/courses/30/lessons/181887
def solution(num_list):
    odd = 0
    even =0
    for i in range(len(num_list)) :
        if i % 2 == 0 :
            odd += num_list[i]
        else :
            even += num_list[i]
    return odd if odd >= even else even