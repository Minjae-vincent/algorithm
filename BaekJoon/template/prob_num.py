def main():
    tmp = [1]
    for i in range(1,1000000):
        if i % 6 == 0: tmp.append(i)

    a = input()
    b = 0
    for i, k in enumerate(tmp):
        b += k
        if b >= int(a):
            print(i+1)
            return

if __name__ == '__main__':
    main()
