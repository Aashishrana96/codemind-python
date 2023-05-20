x=int(input())
c=0
k=[]
for i in range(x):
    z=int(input())
    k.append(z)
p=int(input())
for j in k:
    if j<=p:
        c+=1
    else:
         c+=2
print(c)            