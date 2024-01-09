mylist=[2,4,8,1,9,3,6]
mul=1
for i in range(len(mylist)):
    if i<len(mylist):
        mul=mul*mylist[i]

print("the anser after multiplication of all values in the list is",mul)