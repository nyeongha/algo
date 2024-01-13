def solution(s):
    answer = 0
    ec = 0
    dc = 0
    for n, i in enumerate(s):
        if ec == 0:
            x = i
            ec += 1
        elif i == x:
            ec += 1
        else:
            dc += 1
        if ec > 0 and dc > 0 and ec == dc or n == len(s) - 1:
            answer += 1
            ec = 0
            dc = 0

    return answer