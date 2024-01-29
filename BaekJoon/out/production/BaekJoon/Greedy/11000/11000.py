import heapq
import sys

def main():
    num = int(input())
    lec_list = []

    for _ in range(num):
        p, q = map(int, input().split())
        lec_list.append([p, q])

    lec_list.sort(key=lambda x: x[0])

    tmp_list = []

    heapq.heappush(tmp_list, lec_list[0][1])

    for a in lec_list[1:]:
        if tmp_list[0] > a[0]:
            heapq.heappush(tmp_list,a[1])
        else:
            heapq.heappop(tmp_list)
            heapq.heappush(tmp_list, a[1])

    print(len(tmp_list))
if __name__ == '__main__':
    main()