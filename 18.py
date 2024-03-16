# take a number input from user check if the sum of factros of that number is greater than the original number or not if yes print"Yes"print"No"
#Abundant number
n=int(input())
sum=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum+=i
if sum>n:
    print("Yes")
else:
    print("No")