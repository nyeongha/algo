i = int(input())
arr=[[int(x) for x in input().split()]for y in range(i)]
x=1
for a,b in arr:
    print('Case #%d:'%x,a,'+',b,'=',a+b)
    x+=1