from collections import deque

def solution(s):

    tmp = deque()

    if s[0] == ')' or s.count('(') != s.count(')'): return False

    for value in s:
        if value == '(':
            tmp.append(value)
        else:
            try:
                tmp.pop()
            except:
                return False

    if len(tmp) == 0:
        return True
    else:
        return False
