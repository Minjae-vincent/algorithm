def main():
    a = input()
    a_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for tmp in a_list:
        a = a.replace(tmp,'/')
    print(len(a))

if __name__ == '__main__':
    main()