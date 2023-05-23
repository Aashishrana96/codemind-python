n=input()
for i in range(len(n)):
    n.lower()
    if n.count(n[i])==1:
        print(i)
        break
else:
    print("-1")