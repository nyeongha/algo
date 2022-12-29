total=int(input())
tot2=0
for i in range(int(input())):
    a,b=map(int,input().split())
    tot2+=a*b
if (total==tot2):
    print("Yes")
else:   print("No")