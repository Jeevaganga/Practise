n1=int(input("enter the first number"))
n2=int(input("enter the second number"))

print(n1)
print(n2)

for i in range (2,10):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
