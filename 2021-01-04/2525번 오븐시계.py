x,y=map(int,input().split())
i=int(input())
if y+i>=60:
    print((x+((y+i)//60))%24,(y+i)%60)
elif y+i<60:
    print(x,y+i)