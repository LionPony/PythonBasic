# 전국 대회 선발 고사
# https://school.programmers.co.kr/learn/courses/30/lessons/181851
def solution(rank, attendance):
    rankMap = {}
    for i in range(len(rank)):
        rankMap[rank[i]] = attendance[i]
    answer = []
    for i in sorted(rankMap.keys()):
        if rankMap[i]:
            answer.append(i)
            if len(answer) == 3:
                break
    return 10000*rank.index(answer[0])+100*rank.index(answer[1])+rank.index(answer[2])