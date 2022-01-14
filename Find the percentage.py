#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()   #reads single line of input and splits it into a list of whitespace separated tokens
                                         #name is assigned first token, line a list of the remaining tokens
        scores = list(map(float, line)) #maps float function onto the list of strings, and put the results in a list
        student_marks[name] = scores
    query_name = input()
    average = sum (student_marks[query_name])/3 # uses sum function to sum up elements in list
    print ("%.2f" % average) # or print("{:.2f}".format(average))