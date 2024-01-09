str=input("enter the string")

char1=str[0]
char2=str[-1]

newstr=char2+str[1:-1]+char1

print(newstr)
