import sys
from collections import deque


def main():
    deque_list = deque()

    n = int(input())

    for _ in range(n):
        tmp = list(sys.stdin.readline().split())
        if len(tmp) == 1:
            cli = tmp[0]
            num = 0
        else:
            cli = tmp[0]
            num = tmp[1]

        if cli == 'push_front':
            deque_list.appendleft(int(num))
        elif cli == 'push_back':
            deque_list.append(int(num))
        elif cli == 'pop_front':
            try:
                print(deque_list.popleft())
            except IndexError:
                print(-1)
        elif cli == 'pop_back':
            try:
                print(deque_list.pop())
            except IndexError:
                print(-1)
        elif cli == 'size':
            print(len(deque_list))
        elif cli == 'empty':
            if len(deque_list) == 0:
                print(1)
            else:
                print(0)
        elif cli == 'front':
            try:
                print(deque_list[0])
            except IndexError:
                print(-1)

        elif cli == 'back':
            try:
                print(deque_list[len(deque_list)-1])
            except IndexError:
                print(-1)


if __name__ == '__main__':
    main()
