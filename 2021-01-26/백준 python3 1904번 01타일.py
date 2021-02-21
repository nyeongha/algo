tile={1:1,2:2}
def ti(t):
    for y in range(3,t+1):
        tile[y]=(tile[y-1]+tile[y-2])%15746
    return tile[t]
a=int(input())
print(ti(a))
