class Faculty:
    def __init__(chiru,f_name,dept,id):
        chiru.f_name=f_name
        chiru.dept=dept
        chiru.id=id
    def display(chiru):
        print("faculty information:",chiru.f_name,chiru.dept,chiru.id)
class IT(Faculty):
    pass
obj=Faculty("chiru","it",1204)
obj.display()
obj1=IT("chiranjeevi","IT",1204)
obj1.display()