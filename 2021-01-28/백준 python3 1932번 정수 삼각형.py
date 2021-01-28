aa=int(input())
igle=[0]*aa
ssuu=[0]*aa

for x in range(len(igle)):
    igle[x]=list(map(int,input().split()))
    if len(igle[x])==1:
        ssuu[x]=igle[x]
    elif len(igle)==2:
        ssuu[x]=igle[x][1]
    else:
        a=igle[x-1].index(ssuu[x-1])
        if a==0:
            ssuu[x]=igle[x][a+1]
        elif a==len(igle[x])-1:
            ssuu[x] = igle[x][a - 1]
        else:
            ssuu[x]=(igle[x][a-1] if igle[x][a-1]>igle[x][a+1] else igle[x][a+1])


ssuu[x]=max(igle[x])
print(sum(ssuu))