# def dfs(i, computers, visited):
#     visited[i] = 1
#     for idx, value in enumerate(computers[i]):
#         if (visited[idx] == 0) and (value == 1) and not (i == idx):
#             dfs(idx, computers, visited)

def bfs(i, n, computers, visited):
    visited[i] = 1
    queue = []
    queue.append(i)
    while len(queue) != 0:
        cur = queue.pop(0)
        visited[cur] = 1
        for j in range(n):
            if visited[j] == 0 and computers[cur][j] == 1:
                queue.append(j)


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    # dfs
    # for i in range(n):
    #     if visited[i] == 0:
    #         dfs(i, computers, visited)
    #         answer += 1

    # bfs
    for i in range(n):
        if visited[i] == 0:
            bfs(i, n, computers, visited)
            answer += 1

    return answer