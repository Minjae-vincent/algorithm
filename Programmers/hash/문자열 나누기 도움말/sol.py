def solution(s):
    answer = 0
    is_x = 0
    not_x = 0
    x = ''
    for i in range (len(s)):
        if x == '' : x = s[i]
        if s[i] == x: is_x = is_x + 1
        else : not_x = not_x + 1
        if is_x == not_x: 
            answer = answer + 1
            is_x = 0
            not_x = 0
            x = ''
    if x: answer = answer + 1
        
        
    
    return answer