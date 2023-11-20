from functools import reduce
a=int(input())
b=a
arr=[]
for x in range(1,b+1):
    if a>x:
        arr.append(x)
        a-=x
    elif a<x and (a in arr):
        a+=arr.pop()
        arr.append(a)
        k=(reduce(lambda x,y:x+y,arr))
        if k==b:
            print(arr)
            break
    elif a==x:
        arr.append(x)
        print(arr)
        break
print(len(arr))