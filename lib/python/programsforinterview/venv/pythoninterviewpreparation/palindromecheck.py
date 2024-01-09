s=input("enter the string to check palindrome")
revstr=(s[::-1])

if revstr==s:
    print("the string is palindrome ")

else:
    print("the string is not palindrome")