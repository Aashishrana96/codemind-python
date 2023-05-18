n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for k in range(n):
        l.append(a[k])
    for j in range(m)    :
        l.append(b[j])
    print(*sorted(l))    