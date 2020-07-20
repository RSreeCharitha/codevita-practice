## Given a number 'n' find all possible divisors and print them in increasing order. 

##SI 1 - 10
##SO 1 - 1 2 5 10

n = int(input())
for i in range(1,n+1,1):
    if n%i==0:
        print(i, end=' ')
