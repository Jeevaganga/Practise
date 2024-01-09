#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly
def checkstr(str):
    l = len(str)
    a = 'ing'
    b = 'ly'

    if l < 3:
        return str

    if str[-3:] == 'ing':
        str = str + b
        return str
    else:
        str = str + a
        return str

str=input("enter the string")
print(checkstr(str))