#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range (N):
    command_line = input() # type: str

    if "pop" in command_line:# set.pop() CAN raise keyerror if the set is empty.
        if len(s) > 0:
            s.pop()
    elif "discard" in command_line: #set.discard(value) CANNOT raise keyerror if the discarded value is not in the set
        command,value0 = command_line.split() # str.split() splits the string (command_line) into two strings (command and value0).
        value = int (value0)
        s.discard(value)
    elif "remove" in command_line:
        command,value0 = command_line.split() #set.remove(value) CAN raise keyerror if the discarded value is not in the set
        value = int (value0)
        if value in s:
            s.remove(value)


print (sum(list(s)))

'''
input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
'''