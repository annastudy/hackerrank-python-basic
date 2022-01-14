#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

n = int(input())
s_Eng = set(input().split())
b = int(input())
s_Fren = set(input().split())

total = s_Eng | s_Fren # or s_Eng.union(s_Fren), return a set containing all the elements in both sets without repetition.
print (len(total))

'''
input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''