a=int(input())
arr=[]
arr[0:]=map(int,input().split())
k=0
for x in arr:
    if x==1:
        k+=0
        continue
    elif x==2:
        k+=1
    else:
        for y in range(2,x):
            if x%y==0:
                break
            elif x==y+1:
                k+=1
print(k)