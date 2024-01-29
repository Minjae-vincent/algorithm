def main():
    num = int(input())
    list_tmp = []
    abc = []
    for _ in range(num):
        argument = input()
        tmp_dict = dict()
        tmp_dict['value'] = argument
        tmp_dict['length'] =  len(argument)
        list_tmp.append(tmp_dict)
    list_tmp = sorted(list_tmp, key= lambda x: (x['length'], x['value']))
    for i in range(num):
        if list_tmp[i]['value'] not in abc:
            print(list_tmp[i]['value'])
            abc.append(list_tmp[i]['value'])


if __name__ == '__main__':
    main()