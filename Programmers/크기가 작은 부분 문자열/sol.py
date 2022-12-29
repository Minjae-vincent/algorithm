def solution(t, p):
    answer = 0
    a = len(p)
    #for문 사이즈 = t의 size - p의 사이즈 + 2
    
    for i in range(1, len(t) - len(p) + 2):
        tmp = t[i-1:len(p)+i-1]
        if int(tmp) <= int(p):
            answer = answer + 1
    
    return answer