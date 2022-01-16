#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
from html.parser import HTMLParser
class Myparser (HTMLParser):
    def  handle_starttag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            if attr[1]:
                print ("->",attr[0],">",attr[1])

n = int (input())
html =''
for i in range (n):
    html+=input()
parser = Myparser ()
parser.feed(html)



'''
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

'''