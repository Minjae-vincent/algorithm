import heapq


def solution(operations):
    answer = []
    heap_min = []

    while operations:
        oper_cmd = operations.pop(0).split()
        if oper_cmd[0] == 'I':
            heapq.heappush(heap_min, int(oper_cmd[1]))
        elif oper_cmd[0] == 'D' and heap_min:
            if int(oper_cmd[1]) > 0:
                remove_idx = heap_min.index(heapq.nlargest(1, heap_min, key=None)[0])
                del heap_min[remove_idx]
            else:
                heapq.heappop(heap_min)

    if heap_min:
        answer = [heapq.nlargest(1, heap_min, key=None)[0], heapq.heappop(heap_min)]
    else:
        answer = [0, 0]

    return answer