from collections import deque


def solution(priorities, location):
    deq = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0

    while True:
        cur = deq.popleft()
        if any(cur[1] < tmp[1] for tmp in deq):
            deq.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

    return answer