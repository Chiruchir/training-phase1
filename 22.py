n=1578   
num=n
count=0
sum=0
while n>0:                     
    count+=1
    n//=10
while num>0:
    val=num%10
    sum+=val**count
    count-=1
    num//=10
print(sum)