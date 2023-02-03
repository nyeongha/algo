# from sys import stdin
# n =int(stdin.readline())
# f= list(map(int, stdin.readline().split()))
# max_num=-1
# while f:
#     hap=0
#     for i in f:
#         hap+=i
#         if hap>max_num:
#             max_num=hap
#     f.pop(0)
# print(max_num)

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] = max(a[i], a[i - 1] + a[i])

print(max(a))