s=input()
s.lower()
c=[]
for i in s:
    if i not in c:
        c.append(i)
r=len(c)        
if r==len(s):
    print("True")
else:
    print("False")