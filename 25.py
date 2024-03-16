# write a function to calculate sum of first and lst digit of a number
def fun(a):
    sum=a%10
    while a>=10:
        a//=10
    sum+=a
    print(sum)
a=int(input())
fun(a)