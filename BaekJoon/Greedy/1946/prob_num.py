import sys
from collections import deque

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        q = deque()
        for _ in range(n):
            q.append((tuple(map(int, sys.stdin.readline().split()))))
        q = sorted(q, key = lambda x: (x[0]), reverse= True)
        x, y = q.pop()
        cnt = 1
        while q:
            x1, y1 = q.pop()
            if y > y1:
                cnt += 1
                x, y = x1, y1

        print(cnt)






if __name__ == '__main__':
    main()