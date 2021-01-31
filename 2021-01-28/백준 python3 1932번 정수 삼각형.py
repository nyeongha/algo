aa=int(input())
igle=[0]*aa
ssuu=[0]*aa
su=[0]*aa

for x in range(len(igle)):
    igle[x]=list(map(int,input().split()))
    if len(igle[x])==1:
        ssuu[x]=igle[x][0]
        su[x]=igle[x][0]
    elif len(igle[x])==2:
        su[x]=igle[x][0]
        ssuu[x]=igle[x][1]
    else:
        a=igle[x-1].index(ssuu[x-1])
        b=igle[x-1].index(su[x-1])
        ssuu[x]=(igle[x][a] if igle[x][a]>igle[x][a+1] else igle[x][a+1])
        su[x]=(igle[x][b] if igle[x][b]>igle[x][b+1] else igle[x][b+1])

k=(sum(ssuu) if sum(ssuu)>=sum(su) else sum(su))
print(k)
