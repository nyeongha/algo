import sys
a,b=map(int,sys.stdin.readline().split())
coin=[]
cnt=0
for x in range(a):
    coin.append(int(sys.stdin.readline()))

for x in reversed(coin):
    if b>=x:
        cnt+=b//x
        b=b%x
print(cnt)