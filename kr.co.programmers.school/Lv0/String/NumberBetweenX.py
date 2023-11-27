# x 사이의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/181867
def solution(myString):
    answer = []
    for i in myString.split("x") :
        answer.append(len(i))
    return answer