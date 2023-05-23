s=input()
c=0
k=[]
for i in range(len(s)):
    if s.count(s[i])==1:
        c+=1
        k.append(s[i])
        break
if c>0:
    print(*k)
else:
    print("-1")