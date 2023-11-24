# 리스트 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/181897
def solution(n, slicer, num_list):
    a, b, c = slicer
    b = b+1
    
    if n == 1 :
        return num_list[:b]
    elif n == 2 :
        return num_list[a:]
    elif n == 3 :
        return num_list[a:b]
    elif n == 4 :
        return num_list[a:b:c]