def Roman(N):
    res=""
    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i=12
    while N!=0:
        if num[i]<=N:
            res=res+sym[i]
            N=N-num[i]
        else:
            i-=1
    print(res)
N=int(input())
Roman(N)