import sys


def main():
    input_origin = sys.stdin.readline().strip().split('-')
    tmp_list = []
    for a in input_origin:
        k = 0
        for b in a.split('+'):
            k += int(b)
        tmp_list.append(k)

    if len(tmp_list) == 1:
        print(tmp_list[0])
    else:
        result = tmp_list[0]
        for a in tmp_list[1:]:
            result -= a
        print(result)








if __name__ == '__main__':
    main()
