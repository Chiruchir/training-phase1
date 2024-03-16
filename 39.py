# create a class of name palcements which has a function info which displays the number of placements.
# create another class name dept with function displaywhich will display the names of depts present in the college
# create a class pragati with a function welcome which displays the message welcome to pragati engineering clg we are glad to have on borad 
# and this paragati calss should also display the details about the depts and placements

'''  MULTILEVEL INHERITANCE
 
class Placements():
    def info(self):
        print("we have 670 palcements and still counting")
class dept(Placements):
    def display(self):
        print("Departmets:","\n","CSE","\n","IT","\n","CIVIL","\n","MECHANICAL","\n","EEE")
class pragati(dept):
    def welcome(self):
        print("welcome to pragati engineering clg we are glad to have on borad ")
obj=pragati()
obj.info()
obj.display()
obj.welcome()

'''
     #MUTIPLE INHERITANCE
     
class Placements():
    def info(self):
        print("we have 670 palcements and still counting")
class dept(Placements):
    def display(self):
        print("Departmets:","\n","CSE","\n","IT","\n","CIVIL","\n","MECHANICAL","\n","EEE")
class pragati(dept,Placements):
    def welcome(self):
        print("welcome to pragati engineering clg we are glad to have on borad ")
obj=pragati()
obj.info()
obj.display()
obj.welcome()