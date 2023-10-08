from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)

    answer = 0
    cur_w = 0

    while truck_weights:
        answer += 1
        cur_w -= bridge_queue.popleft()

        if cur_w + truck_weights[0] <= weight:
            cur_w += truck_weights[0]
            bridge_queue.append(truck_weights.popleft())
        else:
            bridge_queue.append(0)

    return answer + bridge_length