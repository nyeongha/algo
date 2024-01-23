def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == num1[i % 5]:
            n[0] += 1
        if answers[i] == num2[i % 8]:
            n[1] += 1
        if answers[i] == num3[i % 10]:
            n[2] += 1

    for nn, i in enumerate(n):
        if i == max(n):
            answer.append(nn + 1)

    return answer