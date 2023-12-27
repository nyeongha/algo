from heapq import heappush, heappop
import sys

input=sys.stdin.readline

num=int(input())
lecture=[list(map(int,input().split())) for _ in range(num)]
lecture.sort()
print(lecture)

hq=[]
heappush(hq,lecture[0][1])
for x,y in lecture[1:num]:
    if x >= hq[0]:
        heappop(hq)
        heappush(hq,y)
    else:
        heappush(hq,y)
print(len(hq))




# 8
# 1 8
# 9 16
# 3 7
# 8 10
# 10 14
# 5 6
# 6 11
# 11 12




# import sys
#
# input = sys.stdin.readline
#
# num = int(input())
# lecture = [list(map(int, input().split())) for _ in range(num)]
# lecture.sort()
#
# hq = [tuple(lecture[0])]
#
# for x, y in lecture[1:num]:
#     hq.sort(key=lambda x: x[1])  # 강의의 종료 시간을 기준으로 우선 순위 큐인 hq를 정렬합니다.
#
#     if x >= hq[0][1]:
#         hq.pop(0)
#         hq.append((x, y))
#     else:
#         hq.append((x, y))
#
# print(len(hq))

