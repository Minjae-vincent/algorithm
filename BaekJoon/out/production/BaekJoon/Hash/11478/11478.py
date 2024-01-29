def main():
    input_str = input()
    result = set()
    for i in range(len(input_str)):
        for j in range(len(input_str)):
            result.add(input_str[i:i+j+1])

    print(len(result))

if __name__ == '__main__':
    main()
