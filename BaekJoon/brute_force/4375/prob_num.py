import sys


def main():
    while True:
        try:
            n = int(input())  # 정수 n
        except:
            break
        tmp = ''
        while True:
            tmp += '1'
            if int(tmp) % n == 0:
                print(len(tmp))
                break

if __name__ == '__main__':
    main()
