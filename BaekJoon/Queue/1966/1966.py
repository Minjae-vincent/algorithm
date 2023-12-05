from collections import deque

def main():
    num = int(input())

    for _ in range(num):
        n, m = map(int, input().split())
        num_list = list(map(int, input().split(' ')))
        num_queue = deque()
        cnt = 0
        for idx, val in enumerate(num_list):
            num_queue.append((val, idx))

        while num_queue:
            tmp_max = max(num_queue)
            if tmp_max[1] == m:
                cnt += 1
                break
            tmp = num_queue.popleft()
            if tmp == tmp_max: cnt += 1
            else:
                num_queue.append(tmp)

        print(cnt)






if __name__ == '__main__':
    main()
