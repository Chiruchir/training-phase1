# craete a class F15 with functions:lights,fans and AC,display
# lights:it prints the colour of the light which is taken as parameter to the function
# fan:it displays the speed in which rotating regulator speed taken as the parameter function
# AC:displays the current room temperature and the outside temperature which are taken as parameters
# display:which displays the difference in outside temperatue and room teperature and also displays the fan speed

class F15:
    def __init__(chiru,a,b):
        print("pragati is one of the waste college in ap ")
        chiru.a=a
        chiru.b=b
        print("Start time",a)
        print("end time:",b)
    def light(chiru,colour):
        print("the room colour is:",colour)
    def fan(chiru,speed):
        chiru.speed=speed
        print("fan speed:",speed)
    def AC(chiru,t1,t2):
        chiru.t1=t1
        chiru.t2=t2
        print("room temperature1:",t1)
        print("outside temperatur:",t2)
    def display(chiru):
        print("differnce b/w temperatures:",abs(chiru.t1-chiru.t2))
        print("fan speed:",chiru.speed)
        print("start time:",chiru.a," ","End time:",chiru.b)
room=F15(9.00,4.00)
room.light("white")
room.fan(50)
room.AC(28,36)
room.display()