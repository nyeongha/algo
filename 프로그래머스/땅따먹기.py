# def solution(land):
#     for i in range(1,len(land)):
#         for j in range(4):
#             temp=0
#             for x in range(4):
#                 if j!=x:
#                     temp=max(temp,land[i][j]+land[i-1][x])
#             land[i][j]=temp
#     answer=max(land[-1])
#     return answer

def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j]+=max(land[i-1][:j]+land[i-1][j+1:])
    answer=max(land[-1])
    return answer