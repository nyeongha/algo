def solution(my_str, n):
    answer = []
    ss = ''
    for nn, i in enumerate(my_str):
        if nn == len(my_str) - 1:  # 마지막요소
            ss += i
            answer.append(ss)
            ss = ''
        else:
            ss += i

        if len(ss) == n:
            answer.append(ss)
            ss = ''
    return answer