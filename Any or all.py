#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
N = int(input())
A = list(map(int,input().split()))

def palindromic_integer (x):
    s=str(x)
    if s==s[::-1]:
        return True
    else:
        return False

if all([i>0 for i in A]):
    if any ([palindromic_integer(i) for i in A]):
        print ("True")
    else:
        print ("False")
else:
    print ("False")  #DO NOT forget this situation

'''
5
-12 9 61 5 14 
'''