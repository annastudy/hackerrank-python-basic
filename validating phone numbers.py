#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re

N = int (input())

for i in range (N):
    S = input()
    match1 = re.search(r'^7\d\d\d\d\d\d\d\d\d$', S)
    match2 = re.search(r'^8\d\d\d\d\d\d\d\d\d$', S)
    match3 = re.search(r'^9\d\d\d\d\d\d\d\d\d$', S)

    if match1 or match2 or match3:
        print ("YES")
    else:
        print ("NO")

'''
input:
2
9587456281
1252478965
'''