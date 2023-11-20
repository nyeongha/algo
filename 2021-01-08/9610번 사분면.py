c={'Q1':0,'Q2':0,'Q3':0,'Q4':0,'AXIS':0}
for x in range(int(input())):
    a,b=map(int,input().split())
    if a>0 and b>0:
        c['Q1']+=1
    elif a<0 and b>0:
        c['Q2']+=1
    elif a<0 and b<0:
        c['Q3']+=1
    elif a>0 and b<0:
        c['Q4']+=1
    else:
        c['AXIS']+=1
for key, value in c.items():
    print('%s: %s'%(key,value))