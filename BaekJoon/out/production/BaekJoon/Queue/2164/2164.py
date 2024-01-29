from collections import deque

def main():
    num = int(input())

    num_queue = deque()
    for i in range(num):
        num_queue.append(i+1)
    result = 0
    while num_queue:
        if len(num_queue) == 1: result = num_queue.popleft()
        else:
            num_queue.popleft()
            num_queue.append(num_queue.popleft())

    print(result)



if __name__ == '__main__':
    main()
