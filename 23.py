#write a function which takes two arguments a and b typecast the value of second argument into integer then multiply both the arguments and print the last digit of the result
def fun(a,b):
    c=int(b)
    sum=a*c
    print(sum%10)
a=int(input())
b=float(input())
fun(a,b)
