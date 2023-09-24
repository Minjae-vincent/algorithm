
import collections

def solution(participant, completion):
    # 기억해야할 점
    # 1. collections.Counter() : 리스트의 각 원소의 개수를 세어준다.
    # 2. collections.Counter() - collections.Counter() : 두 리스트의 원소의 개수를 비교하여 빼준다.
    # 3. list() : 리스트로 변환해준다.
    
    answer = ''
    tmp = collections.Counter(participant) - collections.Counter(completion)
    
    answer = (list)(tmp.keys())[0]
    
    return answer