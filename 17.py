#take an integer as input from the user and check whether if the number is divisible by sum of digits or not
n=int(input())
num=n
sum=0
while n>0:
    sum+=n%10
    n//=10
if num%sum==0:
    print("Yes")
else:
    print("No")