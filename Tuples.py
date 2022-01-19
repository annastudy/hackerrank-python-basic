if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple (integer_list)  #creat a tuple by tuple ()
    print (hash(t))

'''
2
1 2
'''