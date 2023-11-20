i=int(input())
x=2
for y in range(i):
    if i%x==0:
        print(x)
        i=i/x
    else:
        x+=1