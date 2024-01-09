l=[1,2,3,4,1,2,8,5,2,4,1,3,8]
m=[]
for i in l:
    if i not in m:
        m.append(i)

print(m)
