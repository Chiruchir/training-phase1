num=12345
count=0
sum=0
fact=1
print("digits:")
while num>0:
    val=num%10
    print(val)
    sum+=val
    count+=1
    fact*=val
    num//=10
print("count of digits:",count)#count of digits
print("sum of digits:",sum)#sum of digits
print("mulitiplication of digits:",fact)#mulitiplication of digits