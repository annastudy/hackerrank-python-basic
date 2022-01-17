#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    N = int(input())
    list =[]
    for i in range (N):
        command = input().split()

        if command[0]=='insert':
            list.insert(int (command[1]),int(command[2]))
        elif command[0]=='print':
            print (list)
        elif command[0]=='remove':
            list.remove(int (command[1]))
        elif command[0]=='append':
            list.append(int (command[1]))
        elif command[0]=='sort':
            list.sort()
        elif command[0]=='pop':
            list.pop()
        elif command[0]=='reverse':
            list.reverse()

'''
Input sample:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''