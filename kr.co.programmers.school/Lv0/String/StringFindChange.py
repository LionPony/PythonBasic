# 문자열 바꿔서 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181864
def solution(myString, pat):
    translate = ""
    for i in range(len(myString)):
        if myString[i] == "A":
            translate += "B"
        elif myString[i] == "B":
            translate += "A"
    return 1 if pat in translate else 0