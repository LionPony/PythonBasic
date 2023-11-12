# 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935
def solution(n):
    if n % 2 == 0 :
        evens = 0
        for i in range(1, n+1) :
            if i % 2 == 0 :
                evens = evens + i * i
        return evens
    else :
        odds = 0
        for i in range(1, n+1) :
            if i % 2 != 0 :
                odds = odds + i
        return odds