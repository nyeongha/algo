def solution(i, j, k):
    answer = 0
    for _ in range(i,j+1):
        answer+=str(_).count(str(k))
    return answer