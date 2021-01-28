aa=int(input())
igle=[0]*aa
ssuu=[0]*aa

for x in range(len(igle)):
    igle[x]=list(map(int,input().split()))
    if len(igle[x])==1:
        ssuu[x]=igle[x][0]
    if len()
    else:
        a=igle[x-1].index(ssuu[x-1])
        ssuu[x]=(igle[x][a] if igle[x][a]>igle[x][a+1] else igle[x][a+1])
print(ssuu)
