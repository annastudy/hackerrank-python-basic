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