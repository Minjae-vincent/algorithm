def main():
    aeiou = ['a', 'e', 'i', 'o', 'u']
    while True:
        tmp = input()
        flag = True
        if tmp == 'end': break



        if zzz == 5: flag = False
        else:
            for a in tmp[1:]:
                now = a
                if now == a and not now == 'e' or not now == 'o':
                    flag = False
                    break

        if flag:
            print("<" + tmp + ">" " is acceptable.")
        else:
            print("<" + tmp + ">" " is not acceptable.")


if __name__ == '__main__':
    main()
