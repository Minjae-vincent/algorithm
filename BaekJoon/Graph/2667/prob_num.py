import sys
from collections import deque

def bfs(i, j, graph, n):
    q = deque()
    q.append((i, j))

    result = 1

    graph[i][j] = 0

    # 방위
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                result += 1

    return result

def main():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n)]

    result = []

    for i in range(n):
        tmp = sys.stdin.readline().strip()
        for a in tmp:
            graph[i].append(int(a))

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result.append(bfs(i, j, graph, n))

    result.sort()

    print(len(result))
    for a in result:
        print(a)


if __name__ == '__main__':
    main()
