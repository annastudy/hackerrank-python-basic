#https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item) #matrix is a 1D list with elements of strings
matrix_new = [list (x) for x in matrix] # transform data into nested matrix
print (matrix_new)
matrix3 = []
for i in range (m):               #transformed data into matrix3 (1 row m*n colomn) which go through column by column of matrix_new
    for j in range (n):
        matrix3.append(matrix_new[j][i])

print (matrix3)

total="".join(matrix3) #join the elements in matrix3 into a string without separater
print (total)
result = re.sub(r'(?<=[A-Za-z0-9])[\s!@#$%&]+(?=[A-Za-z0-9])',' ',total)  #(?<=A)B(?=C), B is matched with preceding A and following C

print (result)

'''
input sample:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
'''