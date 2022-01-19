
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #print (arr)
    arr1=[x for x in arr if x != max(arr)]
    #print (arr1)
    arr1.sort()
    print (arr1[-1])

'''
5
2 3 6 6 5
'''