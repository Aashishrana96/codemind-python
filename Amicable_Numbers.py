x=int(input())
y=int(input())
s1=0
s2=0
for i in range(1,x):
    if x%i==0:
        s1+=i
    if y%i==0:
        s2+=i
if y==s1 and x==s2:
    print("Amicable")
else:
    print("Not Amicable")