def solution(keymap, targets):
    km_dict={}
    for i in keymap:
        cnt=0
        for j in i:
            cnt+=1
            if j in km_dict:
                if km_dict[j]>cnt:
                    km_dict[j]=cnt
            else:
                km_dict[j]=cnt
    answer=[]
    for i in targets:
        cnt=0
        for j in i:
            if j in km_dict:
                cnt+=km_dict[j]
            if j not in km_dict:
                cnt=-1
                break;
        answer.append(cnt)
    return answer
