# n보다 커질 때까지 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181884
def solution(numbers, n):
    sum = 0
    for i in numbers :
        sum += i
        if sum > n :
            break
    return sum