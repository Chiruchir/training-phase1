# shift all the zeros to the end 
arr=[2,0,1024,0,40,230,0]
brr=[]
count=0
for i in arr:
    if i==0:
        count+=1
    else:
        brr.append(i)
while count>0:
    brr.append(0)
    count-=1
print(brr)

# x,y=0,len(arr)-1
# for i in arr:
#     if i==0:
#         arr[y]=i
#         y-=1
#     else:
#         arr[x]=i
#         x+=1
# print(arr)