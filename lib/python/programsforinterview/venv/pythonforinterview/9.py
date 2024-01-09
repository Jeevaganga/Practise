string='needindeed'

fre={}

for i in string:
    if i in fre:
        fre[i]=fre[i]+1
    else:
        fre[i]=1

print("count of all characters in a string " +  string +" is " + str(fre))