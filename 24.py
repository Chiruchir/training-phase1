#default arguments
def fun(name="chiru",place="srikakulam"):
    print("My name is",name,"and i an from",place)
fun()
fun("Chiranjeevi","kakinada")
#unknowm arguments
def fun(**name):
    print("my name is",name["fname"])
fun(fname="chiru",lname="lothugadda")
#position arguments
def fun(a,b):
    print(a," ",b)
fun(10,20)
#keyword arguments
def fun(a,b):
    print(a," ",b)
fun(b=20,a=10)