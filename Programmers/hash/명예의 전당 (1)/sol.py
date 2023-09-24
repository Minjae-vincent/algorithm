def solution(k, score):
    answer = []
    tmp = []
    for i in range (len(score)):
        if i < k :
            tmp.append(score[i])
        else:
            if min(tmp) < score[i]:
                tmp.remove(min(tmp))
                tmp.append(score[i])
        answer.append(min(tmp))
            
        
    return answer