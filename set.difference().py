#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
s_Eng = set(input().split())
b = int(input())
s_Fren = set(input().split())

only_Eng = s_Eng - s_Fren # or s_Eng.difference(s_Fren), return a set containing  the elements exist only in s_Eng not in s_Fren.
print (len(only_Eng))

'''
input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''