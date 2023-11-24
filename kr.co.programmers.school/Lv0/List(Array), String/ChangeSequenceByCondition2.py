# 조건에 맞게 수열 변환하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181881
def solution(arr):
    ack = 0
    found = False
    
    while found == False :
        
        after = []
        for i in range(len(arr)) :
            if arr[i] >= 50 and arr[i]%2 == 0 :
                after.append(arr[i]/2)
            elif arr[i] < 50 and arr[i]%2 == 1 :
                after.append(arr[i] * 2 + 1)
            else :
                after.append(arr[i])
        if arr == after :
            found = True
        else :
            arr = after
            ack += 1
    return ack