i=int(input())
x=0
while True:
    if 3*(x**2)+(3*x)+1>=i:
        print(x+1)
        break
    else:
        x+=1