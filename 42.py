# create a class ticket which will be the abstarct class inside that create a fuunction bookticket which will be the abstract method and has nothing in it
#create a class makemytrip which will use the bookticket function from ticket class to take the details such as :name,phoneno,email id,journeydate and displays a message thankyou for booking from makemytrip.
# create a class irctc which uses the bokkticket of ticket class take the same details as makemytrip but in the end it will give an option to user to select whether it is oneway or roundtrip if the user option is roundtrip it again asks the user to enter the return date as well and then prints thankyou for choosing irctc else prints thankyou for choosing irctc.
# create a class indigo which takes all the detals as irctc and just asks which mode of transport you want go:train,flight,bus and display thenkyou for choosing indidgo
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip():
    def bookticket(self):
        n=input()
        phone=input()
        email=input()
        jdate=input()
    print("thankyou for booking from makemytrip")
class irctc(makemytrip):
    def bookticket(self):
        makemytrip.bookticket()
        t=input()
        if t=="oneway":
            print("thankyou for choosing irctc.")
        elif t=="roundtrip":
            date=input()
            print("thankyou for choosing irctc.")
class indigo(irctc):
    def bookticket(self):
        makemytrip.bookticket()
        print("which mode do you want:bus,flight,train")
        i=input()
        print("thankyou for choosing indidgo")
        
obj=makemytrip()
obj.bookticket()
# obj1=irctc()
# obj1.bookticket()