arr=[65,79,94,23,107]
n=len(arr)
min=arr[0]

for i in range (0,n):
    if(min>arr[i]):
        min=arr[i]

print("minimum element in the array is",min)