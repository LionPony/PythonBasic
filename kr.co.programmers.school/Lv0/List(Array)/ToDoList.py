# 할 일 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/181885
def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if not finished[i] :
            answer.append(todo_list[i])
    return answer