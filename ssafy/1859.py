from collections import deque

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        input_list = list(map(int, input().split()))
        print(input_list[-1])
        item_num = []

        result = 0
        largest_num = max(input_list)
        largest_index = input_list.index(largest_num)

        deq = deque()
        for a in input_list:
            deq.append(a)

        while deq:
            tmp = deq.popleft()
            # 사는 로직
            if largest_num > tmp and input_list.index(tmp) < largest_index:
                item_num.append(tmp)
                result -= tmp
            # 파는 로직
            elif tmp == largest_num:
                result += len(item_num)*tmp
                if deq:
                    largest_num = max(deq)
                    largest_index = list(deq).index(largest_num)
                    item_num = []

        print('#{} {}'.format(test_case, result))



if __name__ == '__main__':
    main()
