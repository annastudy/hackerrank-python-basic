#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0]) #number of athletes

    m = int(nm[1])  #number of attributes

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split()))) #generate a list of attributes for one athlete

    k = int(input())

    def bubble (array): #go through the array once and adjust the position of each athlete (large value goes down)
        count=0  #will be used as an indicator which determines whether another round of function bubble is necessary
        for i in range (n-1):
            if array[i][k]>array[i+1][k]:
                temp = array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                count+=1
        return(array,count)

    def repeat_check (array,check): #check if repeating function bubble is necessary, if no, repeat; if yes, print.

        if check != 0:
            array,check = bubble (array)
            repeat_check (array,check)
        else:
            print_array (array)

    def print_array (array):
        for i in range (n):
            print (" ".join(map(str,array[i]))) #convert list to strings joint by whitespace.

    array_new,check_new = bubble (arr)
    repeat_check (array_new,check_new)

    '''
    other's solution
        arr.sort(key = lambda x : x[k]) #use list.sort() function with kth attribute as the key
    for i in arr:
        print(*i,sep=' ')
        
    '''
    '''
    input:
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
    '''