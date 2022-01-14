
K = int(input()) #number of people in each group
room_list = list(map(int,input().split()))
room_set = set(room_list)
room_num_list = list (room_set)

for i in room_num_list:
    if room_list.count(i)==1:
        print (i)
        break

# not working
'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
'''