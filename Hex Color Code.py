#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re
n = int (input())
list =[]
for i in range (n):
    s = input()
    if s=="{":
        list.pop()
        continue
    elif "{" in s:
        continue
    else:
        list_match = re.findall (r'#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6}',s) #use | to seperate two patterns within the same ""
        if list_match:
            list = list + list_match

for j in range (len(list)):
    print (list[j])

'''
35
.arrow-up {
	width: 0;
	height: 0;
	border-left: 5px solid transparent;
	border-right: 5px solid transparent;

	border-bottom: 5px solid black;
}

.arrow-down {
	width: 0;
	height: 0;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;

	border-top: 20px solid #f00;
}

.arrow-right {
	width: 0;
	height: 0;
	border-top: 60px solid transparent;
	border-bottom: 60px solid transparent;

	border-left: 60px solid green;
}

#f0f {
	width: 0;
	height: 0;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;

	border-right:10px solid blue;
}

'''