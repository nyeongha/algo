import sys
dic={}
for x in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    if a not in dic:
        dic[a]=[]
        dic[a].append(b)
    else:dic[a].append(b)
for x,y in sorted(dic.items()):
    for _ in sorted(y):
        print(x,_)