a=int(input())
b=list(str(input()))
A=0
B=0
for x in range(a):
    if b[x]=='A':
        A+=1
    else:
        B+=1
if A>B:
    print('A')
elif A<B:
    print('B')
else:
    print('Tie')