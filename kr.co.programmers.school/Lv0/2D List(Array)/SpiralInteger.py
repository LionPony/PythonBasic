# 정수를 나선형으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181832
def solution(n):
    # Set
    answer = [[0 for col in range(n)] for row in range(n)]
    x = 0
    y = 0
    count = 1
    answer[x][y] = count
    count += 1

    while(count <= n*n):
        # Right
        while( y+1 < n and answer[x][y+1] == 0):
            y += 1
            answer[x][y] = count
            count += 1
        # Down
        while( x+1 < n and answer[x+1][y] == 0):
            x += 1
            answer[x][y] = count
            count += 1
        # Left
        while( y-1 >= 0 and answer[x][y-1] == 0):
            y -= 1
            answer[x][y] = count
            count += 1
        # Up
        while( x-1 >= 0 and answer[x-1][y] == 0):
            x -= 1
            answer[x][y] = count
            count += 1
    return answer