import heapq
def solution(k, score):
    answer = []
    sheap=[]

    for i in score:
        heapq.heappush(sheap,i) #최소힙
        if len(sheap)<=k:
            answer.append(min(sheap))
        else:
            heapq.heappop(sheap)
            answer.append(min(sheap))
    return answer