i=0
for x in range(int(input())):
    st=input()
    i+=list(st)==sorted(st,key=st.find)
print(i)