l=[23,12,34,96,45,21,78]
low=l[0]
for i in range(0,len(l)):
    if low>l[i]:
        low=l[i]

print(low)