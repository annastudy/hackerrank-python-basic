#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
T = int(input())
for i in range (T):
    n_A = int(input())
    A = set(map(int,input().split()))
    n_B = int(input())
    B = set(map(int,input().split()))
    if n_B > n_A and len(A|B)==len(B):
        print ("True")
    else:
        print ("False")

'''
input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2


'''