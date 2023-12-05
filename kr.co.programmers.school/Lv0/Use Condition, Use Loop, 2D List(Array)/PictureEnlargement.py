# 그림 확대
# https://school.programmers.co.kr/learn/courses/30/lessons/181836
def solution(picture, k):
    answer = []
    for line in picture :
        large = ""
        for i in range(len(line)) :
            large += line[i] * k
        for j in range(k):
            answer.append(large)
    return answer