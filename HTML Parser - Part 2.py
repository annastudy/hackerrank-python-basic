from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.strip("\n")) == 1: # seperate the content inside comment tag (<!-- -->) by "\n". if only one element, single line.
            print (">>>Single-line Comment")
        else:
            print (">>>Multi-line Comment")
        print (data)

    def handle_data (self, data):
        if data.strip():   #herein, data include all "\n". (?)
            print (">>>Data")
            print (data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'  #use '\n' mark a new line in the string html

parser = MyHTMLParser()
parser.feed(html)
parser.close()

'''
input:
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
'''