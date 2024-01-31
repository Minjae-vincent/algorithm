import sys
import heapq


def main():
    n = int(sys.stdin.readline())
    num_list = []

    for _ in range(n):
        tmp_num = int(sys.stdin.readline())
        if tmp_num > 0:
            heapq.heappush(num_list, -tmp_num)
        else:
            try:
                print(-heapq.heappop(num_list))
            except:
                print(0)



if __name__ == '__main__':
    main()
