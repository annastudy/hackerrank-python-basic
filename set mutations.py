#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
A = set(map(int,input().split()))
N = int(input())

for i in range (N):
    command,num = input().split()
    other_set = set(map(int,input().split()))
    if command == "update":
        A|=other_set
    elif command == "intersection_update":
        A&=other_set
    elif command == "difference_update":
        A-=other_set
    elif command == "symmetric_difference_update":
        A^=other_set

print (sum(list(A)))

'''
input:
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
'''