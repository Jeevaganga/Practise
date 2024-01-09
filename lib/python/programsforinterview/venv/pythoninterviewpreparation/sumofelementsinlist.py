mylist=[34,1,89,45,67,21,43,12,56]
sum=0
x=len(mylist)
for i in range(x):
    if i<x:
        sum=sum+mylist[i]

print("the sum of all elements in the list is",sum)