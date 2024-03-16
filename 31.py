arr=[12,42,23,96,7,18,10,133]
a,b=arr[0],arr[0]
minind,maxind=0,0
for i in range(len(arr)):
    if arr[i]<a:
        a=arr[i]
        minind=i
    if arr[i]>b:
        b=arr[i]
        maxind=i
print(a+b)
arr[maxind]=a+b
arr[minind]=b-a