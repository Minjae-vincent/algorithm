def main():
    l, p, v, i = 1, 1, 1, 1
    while 1:
        l, p, v = map(int, input().split())
        result = 0
        if l == 0 and p == 0 and v == 0: return
        result = get_max(l, p, v)
        print('Case '+ str(i) +': ' + str(result))
        i += 1

def get_max(l, p, v):
    tmp = 0
    while v > 0:
        if v < l:
            tmp += v
            v = 0
        else:
            tmp += l
            v -= p
    return tmp


if __name__ == '__main__':
    main()
