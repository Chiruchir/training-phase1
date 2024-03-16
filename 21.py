#armstrong Number
n=int(input())
n1=n
num=n
count=0
sum=0
while n>0:                     
    count+=1
    n//=10
while num>0:
    val=num%10
    sum+=val**count
    num//=10
if sum==n1:
    print("yes")
else:
    print("No")