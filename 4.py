#check in if a year is leap year or not
#if the year%4==0 and year%100!=0 or if year%400==0 the it is called leap year
a=int(input())
if (a%4==0 and a%100!=0) or a%400==0:
    print("leap year")
else:
    print("not leap year")