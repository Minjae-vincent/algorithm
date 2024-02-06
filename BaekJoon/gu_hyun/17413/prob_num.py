import sys


def main():
    tmp = sys.stdin.readline().strip()
    aa = []
    c = ''
    for a in tmp:
        if a == '<':
            aa.append(c)
            c = ''
            c += a
        elif a == '>':
            c += a
            aa.append(c)
            c = ''
        else:
            c += a
    if len(c) > 0: aa.append(c)

    for a in aa:
        if len(a) != 0:
            if '<' in a:
                print(a, end='')
            else:
                i = 0
                for b in a.split():
                    if i == len(a.split())-1:print(b[::-1], end='')
                    else:print(b[::-1], end=' ')
                    i += 1


if __name__ == '__main__':
    main()
