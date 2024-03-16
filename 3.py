#write a program to check the onroad price of a bike under the conditions:
#1.if price is >72000 then income tax is 10% of exshowroon price and insurance will be 15% of actual price
#2.if price>150000 and price<200000 tax would be 25% and insurance will be 20%
#3.if the price>20000 the tax will be 35% and insurance will be 28%
#4.otherwise min price is 72000.
#on road price of bike=actual price+tax+insurance
a=int(input())
if a>200000:
    print((int)(a+a*0.35+a*0.28))
elif a>150000 and a<=200000:
    print((int)(a+a*0.25+a*0.2))
elif a>=72000 and a<=150000:
    print((int)(a+a*0.10+a*0.15))
else:
    print("min price is 72000 enter a valid price")