# 빈 배열에 추가, 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181860
def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i] :
            for j in range(arr[i]*2):
                X.append(arr[i])
        else :
            for i in range(arr[i]):
                X.pop()
    return X