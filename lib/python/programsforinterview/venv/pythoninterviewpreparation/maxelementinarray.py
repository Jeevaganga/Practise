arr=[20,45,76,32,12]
max=arr[0]
n=len(arr)

for i in range (0,n):
    if (arr[i]>max):
        max=arr[i]

print("maximum number in the given array is",max)
