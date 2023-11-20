#%%
def d(x,y):
    return (((x+y-2)+1)/2)*(x+y-2)
x,y=map(int,input().split())
a=d(x,y)
if (x+y)%2==1:
    print('%d번째'%(a+x))
else:
    print('%d번째'%(a+y))