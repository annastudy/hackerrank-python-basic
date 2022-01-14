
K = int (input())
room_list = list(map(int,input().split()))
#solution 1: using math
#print (int((sum(set (room_list))*K-sum(room_list))/(K-1)))

#soltion 2: using logic

A = set()
B = set()
for i in range (len(room_list)):
    if room_list[i] not in A: # seperate elements in the given room_list into two groups
        A.add(room_list[i])
    else:
        B.add(room_list[i])

print ((A-B).pop()) #use .pop() to get the value in set