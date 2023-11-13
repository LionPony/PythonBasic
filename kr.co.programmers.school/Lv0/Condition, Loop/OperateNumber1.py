# 수 조작하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181926
def solution(n, control):
    for i in range(len(control)) :
        command = control[i]
        if command == "w" :
            n += 1
        elif command == "s" :
            n -= 1
        elif command == "d" :
            n += 10
        else :
            n -= 10
    return n