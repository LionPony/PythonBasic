# A 강조하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181874
def solution(myString):
    answer = ""
    for i in range(len(myString)) :
        if myString[i] == "a" or myString[i] == "A" :
            answer += "A"
        else :
            answer += myString[i].lower()
    return answer