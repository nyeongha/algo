arr=[]
for x in range(int(input())):
    a=input()
    arr.append(a)
arr=sorted(set(arr))
for _ in sorted(arr,key=len):
    print(_)