# write a program to find the seconds smallest negative from the list
arr=[22,-1,42,65,1,-4,6,]
mini=arr[0]
maxi=arr[0]
ind=0
for i in range(len(arr)):
    if arr[i]<mini:
        mini=arr[i]
        ind=i
    if arr[i]>maxi:
        maxi=arr[i]
arr[ind]=maxi
val=arr[0]
for i in range(len(arr)):
    if arr[i]<val:
        val=arr[i]
print(val)
'''
a=999
b=999
for i in range(len(arr)):
    if arr[i]<a:
        b=a;
        a=arr[i]
print(b)

'''
