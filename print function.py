#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    num=0
    for i in range (1,n+1):
        if i // 10 == 0:
            num = (i)+num*10
        elif i // 100 ==0:
            num = (i)+num*100
        else:
            num = (i) + num*1000
    print (str(num))
