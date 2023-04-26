import sys
input=sys.stdin.readline
sys.setrecursionlimit(5000000)



def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if ls[x][y] == 1:
            ls[x][y] = 2
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False
    else:
        return False


while True:
    cnt=0
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    ls=[]
    for i in range(h):
        ls.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if ls[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)
            
                
                
    