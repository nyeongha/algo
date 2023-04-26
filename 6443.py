def ag(t,c):
        if c==len(s):
            k.append(''.join(s))
            return

        for a in t:
            if t[a]>0:
                s.append(a)
                t[a]-=1
                ag(t,c)
                s.pop()
                t[a]+=1

k=[]
s=[]
t=dict()
st=[]
for i in range(int(input())):
     st.append(str(input()))

for i in st:
    for j in i:
          if j in t:
               t[j]+=1
          else:
               t[j]=1
    ag(t,sum(t.values()))
    for kk in sorted(k):
         print(kk)
    t.clear()
    k.clear()

               
    
     