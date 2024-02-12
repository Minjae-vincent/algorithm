import sys
from collections import deque

# BFS
a, b = map(int, sys.stdin.readline())
q = deque()
q.append((a, 1))
flag = True

while q:
    x, y = q.popleft()
    if x > b:
        flag = False
        continue

    elif x == b:
        print(y)
        break

    q.append((int(str(x) + '1'), y+1))
    q.append((x*2, y+1))

if not flag:
    print(-1)


# def main():
#     a, b = map(int, sys.stdin.readline().split())
#     result = 1
#     flag = True
#     while b != a:
#         result += 1
#         tmp = b
#         if b % 10 == 1:
#             b = b // 10
#
#         elif b % 2 == 0:
#             b = b // 2
#
#         if tmp == b:
#             flag = False
#             break
#
#
#     if flag:
#         print(result)
#
#     else:
#         print(-1)
#
#
#
#
#
# if __name__ == '__main__':
#     main()
