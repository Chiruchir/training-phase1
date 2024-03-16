#calculate the difference of sum of numbers that are divisible by 6 and not divisible 6 in the range of first 30 numbers
sum1,sum2=0,0
for i in range(1,31):
    if(i%6==0):
        sum1+=i
    else:
        sum2+=i
val=abs(sum1-sum2)
print(val)