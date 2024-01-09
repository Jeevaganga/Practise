sample=input("enter the string:")

new=str()

for i in sample:
    if i in new:
        new=new+'$'
    else:
        new=new+i

print(new)