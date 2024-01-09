def fact(n):
    if n==0:
        print("factorial of 0 is 1")
        return 1
    elif n==1:
        return 1
    else:
        return(n*fact(n-1))

print("factorial of a number is ",fact(4))