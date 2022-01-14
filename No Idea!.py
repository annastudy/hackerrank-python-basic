#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n,m = map(int, input().split())
    array = list(map(int,input().split()))
    A = set(map(int, input ().split()))
    B = set(map(int, input ().split()))
    happiness = 0

    for i in range (n):
        if array[i] in A:
            happiness += 1
        elif array[i] in B:
            happiness -= 1

    print(happiness)
