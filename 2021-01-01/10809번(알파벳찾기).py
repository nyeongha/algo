a=str(input())
arr=[-1 for x in range(26)]
for _ in a:
    for x in range(97,123):
        if ord(_)==x:
            arr[x-97]=a.index(_)
for _ in arr:
    print(_,end=' ')