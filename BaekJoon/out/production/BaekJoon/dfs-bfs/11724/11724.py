import sys


def dfs(i, node_graph, visited):
    visited[i] = 1
    for idx, value in enumerate(node_graph[i]):
        if visited[idx] == 0 and value == 1:
            dfs(idx, node_graph, visited)


def bfs(i, n, node_graph, visited):
    visited[i] = 1
    queue_list = [i]
    while len(queue_list) != 0:
        tmp = queue_list.pop(0)
        for j in range(n):
            if node_graph[tmp][j] == 1 and visited[j] == 0:
                queue_list.append(j)
                visited[j] = 1


def main():
    n, m = map(int, sys.stdin.readline().split(' '))
    node_graph = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0 for _ in range(n)]
    answer = 0

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split(' '))
        node_graph[x - 1][y - 1] = 1
        node_graph[y - 1][x - 1] = 1

    for i in range(n):
        if visited[i] == 0:
            bfs(i, n, node_graph, visited)
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()
