# 글자 지우기
# https://school.programmers.co.kr/learn/courses/30/lessons/181900
def solution(my_string, indices):
    answer = ""
    for i in range(len(my_string)) :
        if i not in indices :
            answer = answer + my_string[i]
    return answer