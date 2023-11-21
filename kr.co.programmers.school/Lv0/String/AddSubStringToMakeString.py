# 부분 문자열 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181911
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)) :
        s = parts[i][0]
        e = parts[i][1]
        answer = answer + my_strings[i][s:e+1]
    return answer