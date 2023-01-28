line=[]

for i in range(9):
    line.append(list(map(int,input().split())))

max_value = max(map(max, line))

print(max_value)

for i in range(9):
    for j in range(9):
        if line[i][j] == max_value:
            print(i+1,j+1)
        