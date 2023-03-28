import sys

a,b=map(int,sys.stdin.readline().split())
not_listen=set()
not_see=set()

for i in range(a):
    not_listen.add(sys.stdin.readline().strip())

for i in range(b):
    not_see.add(sys.stdin.readline().strip())

not_ls=sorted(list((not_listen)&(not_see)))
print(not_ls)

print(len(not_ls))
for a in not_ls:
    print(a)
