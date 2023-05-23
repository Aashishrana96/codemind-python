s1,s2=map(str,input().split())
s2=list(s2)
c=0
for i in s1:
    if i in s2:
        c+=1
        s2.remove(i)
if(c==len(s1)):
    print("True")
else:
    print("False")
        