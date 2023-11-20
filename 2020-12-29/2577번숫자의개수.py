a=int(input())
b=int(input())
c=int(input())
d=a*b*c
e=str(d)
li=[0,0,0,0,0,0,0,0,0,0]
for x in e:
    for y in range(10):
        if int(x)==y:
            li[y]+=1
            continue
for _ in li:
    print(_)