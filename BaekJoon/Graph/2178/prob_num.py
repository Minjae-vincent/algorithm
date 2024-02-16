import sys
from collections import deque


def bfs(i, j, graph, n, m):
    # 방위 설정
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.appendleft((i, j))

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 1):
                q.appendleft((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]

    # 그래프 생성
    for i in range(n):
        tmp = sys.stdin.readline().strip()
        for a in tmp:
            graph[i].append(int(a))

    sol = bfs(0, 0, graph, n, m)

    print(sol)


if __name__ == '__main__':
    main()
