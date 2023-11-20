arr=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
i=str(input())
to=0
for k in i:
    for x in range(len(arr)):
        for y in range(len(arr[x])):
                if arr[x][y]==k:
                    to+=(x+3)
print(to)