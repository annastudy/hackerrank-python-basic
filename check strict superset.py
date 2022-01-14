#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
A = set(map(int,input().split()))
N = int(input())
count=0
for i in range (N):
    B = set(map(int,input().split()))
    if len(A|B) == len(A) and len(A-B)>0:
        count+=1

if count == N:
    print ("True")
else:
    print ("False")

'''
input:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

'''