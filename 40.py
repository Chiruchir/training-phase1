# POLYMORPHISM
#   OVERLOADING
class Arithmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=Arithmetic()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)

#COMPILE TIME POLYMORPHISM -- FUNCTION OVERLOADING
# ***  pyhton does not support "FUNCTION OVERLOADING"
# it uses last defined function in class 