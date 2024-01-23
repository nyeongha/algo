from collections import deque
def solution(A, B):
    answer=-1
    Ad1=deque(list(A))
    c=len(A)
    B=deque(list(B))
    if Ad1==B:
        answer=0
    else:
        for i in range(1,c):
            Ad1.rotate(1)
            if Ad1==B:
                answer=i
                break
    return answer
# def solution(A,B):
#     return (B*2).find(A)