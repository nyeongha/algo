age={}
for x in range(int(input())):
    a,b=input().split()
    if int(a) not in age:
        age[int(a)]=[]
        age[int(a)].append(b)
    else:age[int(a)].append(b)
for k,v in sorted(age.items()):
    for _ in range(len(v)):
        print(k,v[_])