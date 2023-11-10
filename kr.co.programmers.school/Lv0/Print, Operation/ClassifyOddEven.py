# 홀짝 구분하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181944
a = int(input())
if (a%2 == 0) :
    str = "even"
else :
    str = "odd"
print(f"{a} is {str}")