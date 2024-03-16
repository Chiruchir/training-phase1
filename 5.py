#write a program to check the type of triangle where you take the input from user for three sides and classify it accordingly into equilateral ,iso,scale
a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print("equilateral")
elif a==b or b==c or a==c:
    print("isoseles")
else:
    print("scalance")