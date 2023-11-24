# 원하는 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181878
def solution(myString, pat):
    lowerMyString = myString.lower()
    lowerPat = pat.lower()

    return 1 if lowerMyString.find(lowerPat) != -1 else 0