#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
s_Eng = set(input().split())
b = int(input())
s_Fren = set(input().split())

both = s_Eng & s_Fren # or s_Eng.intersection(s_Fren), return a set containing  the elements exist in both sets.
print (len(both))

'''
input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''