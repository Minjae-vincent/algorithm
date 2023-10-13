import heapq

def solution(jobs):
    answer, now, index = 0, 0, 0
    end_time = -1
    heap = []

    while index < len(jobs):
        for a in jobs:
            if end_time < a[0] <= now:
                heapq.heappush(heap, [a[1], a[0]])
        print(heap)

        if len(heap) > 0:
            cur = heapq.heappop(heap)
            end_time = now
            now += cur[0]
            answer += now - cur[1]
            index += 1
        else:
            now += 1

    return answer // len(jobs)