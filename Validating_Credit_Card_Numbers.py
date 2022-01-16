#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
'''
► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.
'''
import re

N = int (input())
for i in range (N):
    str = input()
    str1 = str.replace('-','')

    m = re.match (r'^([4,5,6][0-9]{3})([0-9]{4}){3}$',str)
    n = re.match (r'^([4,5,6][0-9]{3})(\-[0-9]{4}){3}$',str)
    h = re.match (r'.*(\d)\1{3,}',str) #must add '*' at the beginning, must put \d in group and repeat later for 3 times (intotal 4 times)
    l = re.match (r'.*(\d)\1{3,}', str1)

    if m or n and h == None and l == None :#pay attention to the logic
        print ('Valid')
    else:
        print ('Invalid')

'''
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
'''