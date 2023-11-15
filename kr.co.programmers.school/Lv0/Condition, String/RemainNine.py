# 9로 나눈 나머지
# https://school.programmers.co.kr/learn/courses/30/lessons/181914
def solution(number):
    addDigit = 0
    for i in range(len(number)) :
        addDigit += int(number[i])
    return addDigit%9