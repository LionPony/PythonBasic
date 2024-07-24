# 이차원 배열 대각선 순회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181829
def solution(board, k):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
           if i + j <= k :
            sum += board[i][j] 
    return sum