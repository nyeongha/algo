arr=['c=','c-','dz=','d-','lj','nj','s=','c=','z=']
i=str(input())
for x in arr:
    i=i.replace(x,'1')
print(len(i))