# l로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181834
def solution(myString):
    result = ""
    for i in range(len(myString)):
        if ord(myString[i]) < ord("l"):
            result += "l"
        else:
            result += myString[i]
    return result