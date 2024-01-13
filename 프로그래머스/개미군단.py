def solution(n, lost, reserve):
        # lost1=lost.copy()
        # reserve1=reserve.copy()
        #
        # for i in lost:
        #     if i in reserve:
        #         lost1.remove(i)
        #         reserve1.remove(i)
        # answer = n-len(lost1)
        #
        # lost1.sort()
        # reserve1.sort()
        # for i in lost1:
        #     if i-1 in reserve1:
        #         reserve1.remove(i-1)
        #         answer+=1
        #     elif i+1 in reserve1:
        #         reserve1.remove(i+1)
        #         answer+=1
    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    for i in reserve_del:
        if i - 1 in lost_del:
            lost_del.remove(i - 1)

        elif i + 1 in lost_del:
            lost_del.remove(i + 1)

    answer = n - len(lost_del)

    return answer