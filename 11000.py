import sys
import heapq
num = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for i in range(num)]
lecture=[]

arr.sort()
heapq.heappush(lecture,(arr[0][1],arr[0]))
# print(lecture)
# print(lecture[0][1][1])


for i in range(1,num):

    if lecture[0][1][1] <= arr[i][0]:
        heapq.heappop(lecture)
        # print(lecture)
        heapq.heappush(lecture,(arr[i][1],arr[i]))
        # print(lecture)
    else:
        heapq.heappush(lecture, (arr[i][1],arr[i]))
        # print(lecture)

print(len(lecture))