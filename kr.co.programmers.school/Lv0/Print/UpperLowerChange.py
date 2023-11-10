# 대소문자 바꿔서 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181949
def useSwapcase() :
    str = input()
    str = str.swapcase()
    print(str)

def forString() :
    str = input()
    a = ''
    for i in str :
        if i.isupper() :
            a += i.lower()
        else :
            a += i.upper()
    print(a)
