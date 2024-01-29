from itertools import combinations

def main():
    num, goal = map(int, input().split())
    input_list = list(map(int, input().split()))
    result = 0

    for i in range(1, num+1):
        tmp = list(combinations(input_list, i))
        for j in range(len(tmp)):
            if goal == sum(tmp[j]): result += 1

    print(result)

if __name__ == '__main__':
    main()
