i=int(input())
if i<=12 and i%3==0:
    print(i//3)
elif i%5==0:
    print(i//5)
elif i>=8 and (i%5==3 or i%5==1):
    print(i//5+1)
elif i>=14 and (i%5==2 or i%5==4):
    print(i//5+2)
