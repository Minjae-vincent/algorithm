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
    print(b[a//2])
    # if c[0][1] == c[1][1]:print(c[1][0])
    # elif a == 1: print(b[0])
    # else: print(c[0][0])

    count_list = sorted(Counter(b).items(), key=lambda x: (-x[1], x[0]))
    # print('========================')
    # print(count_list)
    # print('========================')
    if a == 1:
        print(b[0])
    else:
        if count_list[0][1] != count_list[1][1]:
            print(count_list[0][0])
        else:
            print(count_list[1][0])

    print(max(b) - min(b))


if __name__ == '__main__':
    main()
