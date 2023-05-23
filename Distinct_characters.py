z=input().lower()
s=set(z)
c=0
k=[]
for i in s:
    if i>='a' and i<='z':
       k.append(i)
k.sort()       
print(''.join(k))
       