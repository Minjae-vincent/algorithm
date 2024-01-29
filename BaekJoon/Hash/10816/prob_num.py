from collections import Counter


def main():
    n = int(input())
    my_card_list = list(map(int, input().split()))

    m = int(input())
    sample_card_list = list(map(int, input().split()))

    tmp = dict(Counter(my_card_list))
    tmp_keys = tmp.keys()


    for a in sample_card_list:
        if a in tmp_keys: print(tmp.get(a), end=' ')
        else: print(0, end=' ')


if __name__ == '__main__':
    main()
