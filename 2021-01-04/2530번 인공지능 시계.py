a,b,c=map(int,input().split())
i=int(input())
print((a+(c+i)//3600+(b+(c+i)%3600//60)//60)%24,(b+((c+i)%3600)//60)%60,((c+i)%3600)%60)