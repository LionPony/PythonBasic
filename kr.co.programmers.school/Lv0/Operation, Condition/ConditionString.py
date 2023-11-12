# 조건 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181934
def solution(ineq, eq, n, m):
    if ineq == ">" :
        if eq == "=" :
            return int(n >= m)
        else :
            return int(n > m)
    else :
        if eq == "=" :
            return int(n <= m)
        else :
            return int(n < m)