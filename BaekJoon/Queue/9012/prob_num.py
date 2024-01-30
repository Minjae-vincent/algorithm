import sys
from collections import deque


def main():
    n =  int(sys.stdin.readline())
    for _ in range(n):
        input_val = sys.stdin.readline().strip()
        flag = True
        if input_val[0] == ')' or input_val.count('(') != input_val.count(')'):
            print('NO')
            continue
        tmp = deque()
        for val in input_val:
            if val == '(':
                tmp.appendleft(val)
            else:
                try:
                    tmp.pop()
                except:
                    flag = False
        if flag == False:
            print('NO')
        else:
            if len(tmp) == 0:
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()
