# 무작위로 K개의 수 뽑기
# https://school.programmers.co.kr/learn/courses/30/lessons/181858
def solution(arr, k):
    seen =  set([])
    answer = []
    for i in arr :
        if i not in seen:
            seen.add(i)
            answer.append(i)
            if len(answer) == k:
                return answer
    for i in range(k-len(answer)):
        answer.append(-1)
    return answer