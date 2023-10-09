numbers=[1,1,1,1,1]
target=3

leaves = [0]          # 모든 계산 결과를 담자      
count = 0 

for num in numbers : 
    temp = []# 자손 노드 
    for leaf in leaves : 
        temp.append(leaf + num)    # 더하는 경우 
        print(temp)
        temp.append(leaf - num)    # 빼는 경우 
        print(temp)

    leaves = temp 


print((leaves.count(target)))
