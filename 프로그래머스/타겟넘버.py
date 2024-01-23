def solution(numbers, target):
    answer = 0
    parents = [0]  # 부모 leaf값
    for i in numbers:
        temp = []
        for parent in parents:
            temp.append(parent + i)
            temp.append(parent - i)
        parents = temp.copy()

    answer = parents.count(target)
    return answer