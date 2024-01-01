def solution(lottos, win_nums):
    ll={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt=0
    for i in win_nums:
        if i in lottos:
            cnt+=1
    zero=lottos.count(0)
    answer=[ll[cnt+zero],ll[cnt]]
    return answer