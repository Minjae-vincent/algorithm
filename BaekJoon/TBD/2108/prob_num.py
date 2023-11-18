import sys
from collections import Counter

def main():
    a = int(sys.stdin.readline())
    b = []

    for _ in range(a):
        b.append(int(sys.stdin.readline()))

    b.sort()

    c = dict(Counter(b))

    c = sorted(c.items(), key= lambda x: x[1], reverse=True)

    print(round(sum(b)/a))
    print(b[round(a/2)])
    if c[0][1] == c[1][1]:
        if c[0][0] > c[1][0]: print(c[0][0])
        else: print(c[1][0])
    else: print(c[0][0])
    print(b[a-1] - b[0])

if __name__ == '__main__':
    main()
