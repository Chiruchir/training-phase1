a=int(input())
for i in range(2,a+1):
    if i==a:
        print("prime")
    elif a%i==0:
        print("not prime")
        break