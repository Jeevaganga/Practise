#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

str1=input("enter first string")
str2=input("enter second string")

new1=str2[0:2]+str1[2:]
new2=str1[0:2]+str2[2:]



print(new1+" "+new2)