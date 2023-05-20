def recr_fact(n):
    if n==1:
        return 1
    else:
        return n*recr_fact(n-1)
t=int(input())
for i in range(t):
    n=int(input())
    if n==0:
        print("1")
    elif n>0:
        print(recr_fact(n))