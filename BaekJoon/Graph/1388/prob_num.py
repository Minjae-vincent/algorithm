import sys


def main():
    n, m = sys.stdin.readline().strip().split()
    input_list = []
    for _ in range(int(n)):
        tmp_input = sys.stdin.readline().strip()
        tmp_list = []
        for i in range(len(tmp_input)):
            tmp_list.append(tmp_input[i])
        input_list.append(tmp_list)


    print(input_list)





if __name__ == '__main__':
    main()
