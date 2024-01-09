mylist=[1,2,3,4,5,6,3,7,10,3,2,9,4,1,7,4,8,2]
x=int(input("enter a number to find its number of occurance "))
count=0
for i in mylist:
    if x==i:
        count=count+1


print("the number",x,"occured",count,"times")