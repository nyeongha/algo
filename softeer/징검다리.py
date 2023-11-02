import sys

rock_len=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
dp=[1 for i in range(rock_len)]

for n,i in enumerate(arr[1:],start=1):
    for n1,j in enumerate(arr[:n]):
        if i>j:
            dp[n]=max(dp[n1]+1,dp[n])
print(max(dp))






# 5
# 1 9 2 4 3

# 6
# 2 1 9 1 4 3