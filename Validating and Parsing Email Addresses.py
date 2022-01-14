#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import email.utils
import re

n = int(input())

for i in range (n):
    name_addr = email.utils.parseaddr (input())
    email_addr = name_addr[1]
    if re.search (r'^[A-Za-z][\w.-]+@[A-Za-z]+\.[A-Za-z]{1,3}$',email_addr): #pay attention to the boundary using ^ and $
        print (email.utils.formataddr ((name_addr[0]  ,email_addr)))  #. -> any character except new line
                                                                      #/.  ->  dot
                                                                      #\d  -> digit
                                                                       # d  -> letter d
                                                                        #{}   -> number of repetition

'''
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
'''