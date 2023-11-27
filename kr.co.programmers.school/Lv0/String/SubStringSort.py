# 문자열 잘라서 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181866
def solution(myString):
    myString = myString.split("x")
    myString = [i for i in myString if i]
    return sorted(myString)