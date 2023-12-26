from functools import reduce
def solve(d):
    ans=reduce(lambda x,y:x+y,d)
    return ans
#n=int(input() )#이문제는 입력이 없고 함수만 작성함
#a=[]
#for k in range(n):
#    a.append(int(input()))
#print(solve(a))