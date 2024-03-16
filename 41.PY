#OVERRINDING
class father:
    def bike(self):
        print("Royal enfield")
    def laptop(self):
        print("HP victus ")
class child(father):
    def laptop(self):
        print("Macbookpro")
obj=child()
obj.bike()
obj.laptop()