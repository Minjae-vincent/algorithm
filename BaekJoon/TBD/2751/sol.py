
import sys
def main():
    num = int(input())
    tmp = []
    for _ in range(num):
        tmp2 = int(sys.stdin.readline().strip())
        tmp.append(tmp2)
    tmp.sort()
    list(map(lambda x: print(x), tmp))

if __name__ == '__main__':
    main()