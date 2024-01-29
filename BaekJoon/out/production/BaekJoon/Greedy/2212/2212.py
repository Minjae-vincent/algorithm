

def main():
    n = int(input())
    k = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    len_list = []


    for i in range(len(n_list) - 1):
        len_list.append(n_list[i+1] - n_list[i])

    len_list.sort(reverse=True)
    # len_list의 reverser 중, 0 ~ K-1개는 기지국 사이의 거리라 생각하기
    print(sum(len_list[k-1:]))


if __name__ == '__main__':
    main()