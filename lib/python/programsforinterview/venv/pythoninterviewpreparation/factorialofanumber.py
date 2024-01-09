number=int(input("enter the number to find its factorial"))
factorial=1

if number<0:
    print("factorial of this number does not exists")
elif number==0:
    print("factorial of this number is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("factorial of a number",i,"is ",factorial)