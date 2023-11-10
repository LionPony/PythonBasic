# 문자열 겹쳐쓰기
# https://school.programmers.co.kr/learn/courses/30/lessons/181943
def solution(my_string, overwrite_string, s) :
    result = ''
    for i in range(0, len(my_string)) :
        if s <= i < s+len(overwrite_string) :
            result = result+overwrite_string[i-s]
        else :
            result = result+my_string[i]
    return result