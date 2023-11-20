import sys
dic={}
for x in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    if b not in dic:
        dic[b]=[]
        dic[b].append(a)
    else:dic[b].append(a)
for x,y in sorted(dic.items()):
    for _ in sorted(y):
        print(_,x)