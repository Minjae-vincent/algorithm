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

        while True:
            if num_queue[0][0] == max(num_queue, key=lambda x:x[0])[0]:
                cnt += 1
                if num_queue[0][1] == m:
                    print(cnt)
                    break
                else: num_queue.popleft()
            else:
                num_queue.append(num_queue.popleft())







if __name__ == '__main__':
    main()
