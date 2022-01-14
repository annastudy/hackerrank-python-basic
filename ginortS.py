#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
S = input()
lower_case = []
upper_case = []
odd_digit = []
even_digit = []

for i in S:                                 #use ASCII code to seperate alphanumeric characters into four lists.
    if ord(i)>=97 and ord(i)<=122:          #pay attention to the boundary.
        lower_case.append (i)
    elif ord(i)>=65 and ord(i)<=90:
        upper_case.append (i)
    elif (ord(i)-48) % 2 == 1:
        odd_digit.append (i)
    elif (ord(i)-48) % 2 == 0:
        even_digit.append (i)

lower_case.sort()                   #sort each list respectively.
upper_case.sort()
odd_digit.sort()
even_digit.sort()

result = lower_case+upper_case+odd_digit+even_digit  #join the four lists
print (''.join(result))  # join the characters in list into a string.