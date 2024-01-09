str=input("enter the string")
str1=''

for i in range(0,len(str)):
    if i%2==1:
        str1=str1+str[i]

print(str1)