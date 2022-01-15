#https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
from html.parser import HTMLParser

class Myparser (HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :',tag)
        for (name, attr) in attrs:
            print ('->', name,'>', attr)

    def handle_endtag(self, tag):
        print ('End   :',tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for (name, attr) in attrs:
            print ('->', name,'>', attr)
n = int(input())
p = Myparser ()

for i in range (n):
    p.feed(input())

'''
input:
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

'''
