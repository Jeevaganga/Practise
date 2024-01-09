           #converting comma separated values into list and tuple#

values=input("enter some comma separated values:")

list=values.split(",")
tuple=tuple(list)

print('list:',list)

print('tuple:',tuple)