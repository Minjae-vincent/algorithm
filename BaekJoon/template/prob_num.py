def main():
    tmp = []
    out_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while True:
        input_str = input()
        if input_str in out_list:
            print(''.join(tmp))
            break
        else: tmp.append(input_str)


if __name__ == '__main__':
    main()
