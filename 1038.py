from itertools import combinations
CL=['0','1','2','3','4','5','6','7','8','9']
n=int(input())
ss=[]

for i in range(1,11):
    a=list(combinations(CL,i))
    for i in a:
        k=sorted(list(i),reverse=True)
        ss.append(int(''.join(k)))
ss.sort()
if n<1023:
    print(ss[n])
else:
    print(-1)

