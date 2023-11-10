# 문자 리스트를 문자열로 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181941
def solution(arr):
    answer = ''
    for i in range(0, (len(arr))) :
        answer = answer + arr[i]
    return answer