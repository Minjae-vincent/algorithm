from collections import deque


def solution(prices):
    answer = []

    prices_queue = deque(prices)

    while prices_queue:
        tmp_a = prices_queue.popleft()
        tmp = 0

        for a in prices_queue:
            tmp += 1
            if tmp_a > a: break
        answer.append(tmp)

    return answer