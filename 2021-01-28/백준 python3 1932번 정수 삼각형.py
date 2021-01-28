aa=int(input())
igle=[0]*aa
ssuu=[0]*aa

for x in range(len(igle)):
    igle[x]=list(map(int,input().split()))


ssuu[x]=max(igle[x])
print(sum(ssuu))