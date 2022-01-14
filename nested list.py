#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    name_list=[]
    score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
    records=[]
    for i in range (len(name_list)):
        records.append([name_list[i],score_list[i]])

    rev_score = sorted(score_list,reverse=True)

    for i in range (len(score_list)):
        if rev_score[-1] != rev_score[-2]:
            second_low_score = rev_score[-2]
            break
        else:
            rev_score.pop()

    second_low_name=[]
    for i in range (len(name_list)):
        if score_list [i] == second_low_score:
            second_low_name.append(name_list[i])

    second_low_name.sort()
    for i in range (len(second_low_name)):
        print (second_low_name[i])
