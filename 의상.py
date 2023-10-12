def solution(clothes):
    answer=1
    dic={}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:dic[i[1]]=1

    for value in dic.values():
        answer *=(value + 1)
    return answer-1

clothes=[
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
]
solution(clothes)
