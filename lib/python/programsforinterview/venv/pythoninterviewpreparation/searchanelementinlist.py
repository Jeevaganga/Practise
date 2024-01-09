mylist=[23,45,21,14,7,89,62,59,4]
n=int(input("enter an element to search"))
count=0

for i in range(0,len(mylist)):
    if n==mylist[i]:
        count=count+1
        break
    else:
        continue

if count>0:
    print("the number is present in the given list")

else:
    print("th number is not in the given list")