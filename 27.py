#write a recursive function to count no of digits of a number
def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
n=int(input())
print(count(n))