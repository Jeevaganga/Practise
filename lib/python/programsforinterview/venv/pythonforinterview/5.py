          # to print n+nn+nnn #

a=int(input("enter the number: "))

#s1=n
#s2=n*10+n
#s3=n*100+n*10+n
#sum=s1+s2+s3

#print(sum)


n1=int("%s" %a)
n2=int("%s%s" %(a,a))
n3=int("%s%s%s" %(a,a,a))

print(n1+n2+n3)