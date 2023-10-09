import sys
sys.stdin = open('input.txt')



# 총 10개의 테스트케이스
# 첫 번째 줄에는 건물의 개수 N
# 그 다음 줄에는 N개의 건물의 높이

for i in range(10):
    N=int(input())
    stack=[0 for _ in range(N)]
    visit=[-1 for __ in range(N)]
    height=list(map(int,input().split()))
    for num in range(2,N-2):
        ll=[height[num-1],height[num-2],height[num+1],height[num+2]]
        if height[num]>height[num-1] and height[num]>height[num-2] and height[num]>height[num+1] and height[num]>height[num+2]:
            visit[num]=height[num]-max(ll)
        else:
            visit[num]=0

    print("#{} {}".format(i+1,sum(visit)+4))
