def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = int(a)+int(b)
    else:
        answer = int(a)-int(b)
    return answer