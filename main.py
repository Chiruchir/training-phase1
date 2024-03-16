from userlogin import *
from products import *
class order:
    print("existing user Or new user")
    t=int(input())
    obj=landr()
    obj1=products()
    if t==1:
        n=input()
        p=input()
        e=input()
        obj.registration(n,p,e)
        print("registration successful")
    elif t==2:
        n=input()
        p=input()
        if obj.userlogin(n,p):
            print("login successful")
            print("available product types:1.electronics,2.fahion,3.books")
            n=input("enter your choice:")
            if n=="electronics":
                print("welcome to electronic store:")
                print("available products:1.laptops,2.mobiles")
                m=input("enter your choice")
                if m=="laptops":
                    q=10
                    obj1.add(n,m,q)
                elif m=="mobiles":
                    q=10
                    obj1.add(n,m,q)
            elif n=="fashion":
                print("welcome to fashion store:")
                print("available products:1.shirt,2.jeans")
                m=input("enter your choice")
                if m=="jeans":
                    q=10
                    obj1.add(n,m,q)
                elif m=="shirts":
                    q=10
                    obj1.add(n,m,q)
            elif n=="books":
                print("welcome to electronic store:")
                print("available products:1.schand,2.cengage")
                m=input("enter your choice")
                if m=="schand":
                    q=10
                    obj1.add(n,m,q)
                elif m=="cengage":
                    q=10
                    obj1.add(n,m,q)   
        else:
            print("wrong details try again")
        