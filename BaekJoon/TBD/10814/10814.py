
def main():
    num = int(input())
    list_tmp = []
    abc = []
    for i in range(num):
        age, name = input().split()
        tmp_dict = dict()
        tmp_dict['name'] = name
        tmp_dict['age'] =  int(age)
        tmp_dict['order'] = int(i)
        list_tmp.append(tmp_dict)
    list_tmp = sorted(list_tmp, key= lambda x: (x['age'], x['order']))
    for i in range(num):
        print(list_tmp[i]['age'], list_tmp[i]['name'])


if __name__ == '__main__':
    main()