import sys


def main():
    test_num = int(sys.stdin.readline())
    for _ in range(test_num):
        n, m = map(int, sys.stdin.readline().split())
        tmp_graph = [[] for i in range(n+1)]
        check_list = [0]*(n+1)
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            tmp_graph[a].append(b)
            tmp_graph[b].append(a)

        def dfs(idx, ans):
            check_list[idx] = 1
            for i in tmp_graph[idx]:
                if check_list[i] == 0:
                    ans = dfs(i, ans+1)

            return ans
        ans = dfs(1,0)
        print(ans)



if __name__ == '__main__':
    main()
