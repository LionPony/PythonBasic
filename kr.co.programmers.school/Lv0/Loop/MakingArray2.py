# 배열 만들기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181921
def solution(l, r):
    arr = [False] * digitCount(r)
    answer = []
    answer = backtracking(arr, 0, answer, l, r)
    answer.sort()
    return answer if len(answer) > 0 else [-1]

def backtracking(checkArr, start, answer, l, r) :
    result = ""
    for i in checkArr :
        if i :
            result = result + "5"
        else :
            result = result + "0"
    if int(result) >= l and int(result) <= r :
        answer.append(int(result))
    for i in range(start, len(checkArr)) :
        checkArr[i] = True
        backtracking(checkArr, i + 1, answer, l, r)
        checkArr[i] = False
    return answer
        
def digitCount(number) :
    count = 0
    while(number > 0) :
        number //= 10
        count += 1
    return count