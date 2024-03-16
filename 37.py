# 3 car companies tayota,mahindra,mercedes
# take the input from user for the car company name and int the input message give user three options 
# 1.this user input company name those as the input/argument to model name function which welcomes the user accordingly to the company name.
# #   ask the user to enter the specific model name for that company
# # 2.the second function whose name if variant according to the company name and car model will user should be asked to enter the variant he would like to choose from petrol,diesel
# # 3.the last function display accroding to the car company car modelname and car variant first its exshowrrom price should be displayed 
# #   and then its onroad price shoulss be displayed,which is calculated as exshowroom price+cgst+sgst+insurance.the sgst,cgst and insurance all the three have common value throughout car showroom
class carshowroom:
    def carcompany(self,name):
        self.cgst=0.18*3
        self.a=name
        match name:
            case "tayota":
                print("welcome to toyota familly:")
                model=input()
                print("variants are:petrol,diesel")
                self.model=model
                self.t=input()
                self.price=self.variant(model,name,self.t)
                self.display(name,model,self.t,self.price)
            case "mahindra":
                print("welcome to mahindra family")
                model=input()
                print("variants are:petrol,diesel")
                self.model=model
                self.t=input()
                self.price=self.variant(model,name,self.t)
                self.display(name,model,self.t,self.price)
            case "mercedes":
                print("welcomes to mercedes family")
                model=input()
                print("variants are:petrol,diesel")
                self.model=model
                self.t=input()
                self.price=self.variant(model,name,self.t)
                self.display(name,model,self.t,self.price)
    def variant(self,m,n,t):
        if m=="a" and n=="tayota" and t=="petrol":
            return 5000000
        elif m=="b" and n=="tayota" and t=="diesel":
            return 24000000
        elif m=="a" and n=="mercedes" and t=="petrol":
            return 32000000
        elif m=="b" and n=="mercedes" and t=="diesel":
            return 763400000
        elif m=="a" and n=="mahindra" and t=="petrol":
            return 1000000
        elif m=="b" and n=="mahindra" and t=="diesel":
            return 10089000
    def display(self,n,m,t,price):
        if n=="tayota" and m=="a" and t=="petrol":
            print("onroad price is:",price)
            print("exshowroom price is",price+price*self.cgst)
        elif n=="tayota" and m=="b" and t=="diesel":
            price=2000000
            print("onroad price is:",price)
            print("exshowroom price is",price+price*self.cgst)
        elif n=="mahindra" and m=="a" and t=="petrol":
            price=1500000
            print("onroad price is:",price)
            print("exshowroom price is",price+price*self.cgst)
        elif n=="mahindra" and m=="b" and t=="diesel":
            price=10000000
            print("onroad price is:",price)
            print("exshowroom price is",price+price*self.cgst)
        elif n=="mercedes" and m=="a" and t=="petrol":
            price=50000000
            print("onroad price is:",price)
            print("exshowroom price is",price+price*self.cgst)
        elif n=="mercedes" and m=="b" and t=="diesel":
            price=25000000
            print("onroad price is:",price)
            print("exshowroom price is",price+price*self.cgst)
car=carshowroom()
companyname=input()
car.carcompany(companyname)