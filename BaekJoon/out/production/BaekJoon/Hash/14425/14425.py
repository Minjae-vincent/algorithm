import sys
def main():
    n, m = map(int, input().split())
    tmp1 = []
    result = 0
    for _ in range(n):
        tmp1.append(input())
    for _ in range(m):
        a = input()
        if a in tmp1: result += 1

    print(result)



if __name__ == '__main__':
    main()
