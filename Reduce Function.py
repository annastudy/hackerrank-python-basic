#https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce (lambda x,y:x*y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

'''
Input sample:
3
1 2
3 4
10 6
'''