# https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re
def check_match_1 (str):
    return re.search (r'[A-Z].*[A-Z]',str)

def check_match_2 (str):
    return re.search (r'\d.*\d.*\d',str)

def check_match_3 (str):
    return re.search (r'[^a-zA-Z0-9]',str)

def check_match_4 (str):
    return re.search (r'(.).*\1+',str)

def check_match_5 (str):
    return re.search (r'.{10}',str)

for i in range (int(input())):
    str = input()
    if check_match_1 (str) != None and check_match_2 (str)!= None and check_match_3 (str)== None and check_match_4 (str)== None and check_match_5 (str)!= None:
        print ('Valid')
    else:
        print ('Invalid')

'''
Input:
2
B1CD102354
B1CDEF2354
'''
