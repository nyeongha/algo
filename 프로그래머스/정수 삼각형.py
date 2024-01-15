def solution(triangle):
    answer = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i==0 and j==0:
                continue
            elif j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    answer=max(triangle[len(triangle)-1])
    return answer