arr=[]
for x in range(9):
    arr.append(int(input()))
raa=sorted(arr)
print(raa[8])
print(arr.index(raa[8])+1)