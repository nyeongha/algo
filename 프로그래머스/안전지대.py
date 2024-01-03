def solution(board):
    answer = 0
    n = len(board)
    check = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                check[i][j] = 1
                inspect(i, j, check, n)
    for i in check:
        answer += i.count(0)
    return answer


def inspect(x, y, check, n):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for xx, yy in zip(dx, dy):
        if 0 <= (x + xx) < n and 0 <= (y + yy) < n and check[x + xx][y + yy] == 0:
            check[x + xx][y + yy] = 1
