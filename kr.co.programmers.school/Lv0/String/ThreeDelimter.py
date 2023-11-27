# 세 개의 구분자
# https://school.programmers.co.kr/learn/courses/30/lessons/181862
import re
def solution(myStr):
    answer = re.split("[a|b|c]", myStr)
    answer =  [i for i in answer if i]
    return answer if len(answer) >= 1 else ["EMPTY"]