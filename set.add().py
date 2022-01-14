#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == "__main__":
    N = int(input())
    country = set()  # create a set; cannot use country ={}, because this is creating a dictionary
    for i in range (N):
        new = input()
        if new not in country:
            country.add(new)

    print (len(country))