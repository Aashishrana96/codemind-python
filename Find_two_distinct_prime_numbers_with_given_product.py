def prime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    else:
        return True
n=int(input())
c=0
for j in range(2,n+1):
    for k in range(2,n+1):
        if(prime(j) and prime(k)):
            if(j*k==n and j<k):
                print(j,k,end=' ')
                c+=1
                break
if(c==0):
    print('-1')
                