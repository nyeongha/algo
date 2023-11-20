a,b,c=map(int,input().split())
x=1
if b-c<0:
    print(a//(c-b)+1)
else:
    print(-1)