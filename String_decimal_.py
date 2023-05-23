n=int(input())
c=0
for i in range(n):
    
    s=list(map(str,input().split()))
    k=len(s)
    for i in s:
        c=0
        if i.isdigit():
            c+=1
    if c==k:
        print("True")
    else:
        print("False")