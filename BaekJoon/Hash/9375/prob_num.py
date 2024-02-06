import sys
from collections import Counter


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        cloth_dict = dict()
        n = int(sys.stdin.readline())
        for _ in range(n):
            name, cloth_type = sys.stdin.readline().strip().split()
            cloth_dict[name] = cloth_type

        result = 1

        for a in list(Counter(cloth_dict.values()).values()):
            result *= a+1

        print(result-1)
        # for keys in Counter(cloth_dict.values()):
        #     print(keys)



if __name__ == '__main__':
    main()
