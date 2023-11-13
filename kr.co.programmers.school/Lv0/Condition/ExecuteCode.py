# 코드 처리하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181932
def solution(code):
    ret = ''
    mode = False
    
    for i in range(0, len(code)) :
        if code[i] == "1" :
            if mode :
                mode = False
            else :
                mode = True
        else :
            if mode :
                if i%2 != 0 :
                    ret = ret + code[i]
            else :
                if i%2 == 0 :
                    ret = ret + code[i]
    return 'EMPTY' if len(ret) == 0 else ret