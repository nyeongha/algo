tile={1:1,2:2}
def ti(x):
    for y in range(3,x+1):
        tile[y]=(tile[y-1]+tile[y-2])%1574
    return tile[x]
a=int(input())
print(ti(a))
