a,b=map(int,input().split())
li=[]
li[0:a] = map(int, input().split())
k=[]
for x in li:
    if x<b:
        k.append(x)
    else:
        continue
print(' '.join(map(str,k)))