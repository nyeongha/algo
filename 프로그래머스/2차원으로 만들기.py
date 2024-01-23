def solution(num_list, n):
    answer = []
    kk=[]
    for i in num_list:
        if len(kk)<n:
            kk.append(i)
        if len(kk)==n:
            answer.append(kk)
            kk=[]
    return answer