s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=0
s1=s1.split()
s2=s2.split()
for i in s1:
    if i in s2:
        c+=1
print(c)  