import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()

    k = set()

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1

    for i in range(n):
        if graph[0][i] == 1:
            q.appendleft(i)
            k.add(i)
            graph[0][i] = 0
            graph[i][0] = 0

    while q:
        tmp = q.popleft()
        for i in range(n):
            if graph[tmp][i] == 1:
                q.appendleft(i)
                k.add(i)
                graph[tmp][i] = 0
                graph[i][tmp] = 0

    print(len(k))


if __name__ == '__main__':
    main()
