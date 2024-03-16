n=int(input())
a=n
num=0
while n>0:
    num=num*10+n%10
    n//=10
if a==num:
    print("Yes")
else:
    print("No")