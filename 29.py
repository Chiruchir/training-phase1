# write the code of armstring using recursion
def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
def arm(n):
    if n==0:
        return 0
    return (n%10)**c+arm(n//10)
n=int(input())
c=count(n)
num=arm(n)
if num==n:
    print("Yes")
else:
    print("No")