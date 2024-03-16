# create an atm System
#1.displaying the remaining amount in the atm
#2.authentication of user,if the user is authenticated then give him follwing options to choose:
#   1.check balance
#   2.cash withdrwal update the balance rupay-2000,visa-5000,mastercard=8499
#   3.cash deposit update the balance
#3.mini statement of last three transactions
#4.rupay,visa,mastercard 

import display
import authentication
obj2=authentication.security()
class Acc:
    balance=1000000
    def check(self):
        print(self.balance)
    def withdraw(self,t,a):
        if t=="rupay" and a>2000:
            print("amount sould less than 2000")
        elif t=="visa" and a>5000:
            print("amount sould less than 5000")
        elif t=="mastercard" and a>8499:
            print("amount sould less than 8499")
        elif t=="rupay":
            print("withdraw successful")
            balance-=a
        elif t=="visa":
            print("withdraw successful")
            balance-=a
        else:
            print("withdraw successful")
            balance-=a
    def deposit(self,a):
        print("deposit successful")
        balance+=a
class ATM:
    def __init__(slef):
        print(display.amount)
        print("selct card:rupay,visa,mastercard")
        t=input()
        if t=="rupay":
            n=input()
            m=input()
            if obj2.aut(n,m):
                print("login success please choose option:check balance,withdraw,deposit")
                x=input()
                if x==1:
                    object.check()
                elif x==2:
                    a=int(input())
                    object.withdraw(t,a)
                else:
                    a=input()
                    object.deposit(a)
        elif t=="visa":
            n=input()
            m=input()
            if obj2.aut(n,m):
                print("login success please choose option:check balance,withdraw,deposit")
                x=input()
                if x==1:
                    object.check()
                elif x==2:
                    a=int(input())
                    object.withdraw(t,a)
                else:
                    a=input()
                    object.deposit(a)
        elif t=="mastercard":
            n=input()
            m=input()
            if obj2.aut(n,m):
                print("login success please choose option:check balance,withdraw,deposit")
                x=input()
                if x==1:
                    object.check()
                elif x==2:
                    a=int(input())
                    object.withdraw(t,a)
                else:
                    a=input()
                    object.deposit(a)
o=ATM()
object=Acc()
    