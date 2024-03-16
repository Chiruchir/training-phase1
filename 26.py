# write login function which accepts the user only when the username and password are same and displays a message login successful otherwise it keeps asking the user to enter the credentials until they are correct
def login():
    a=input()
    b=input()
    if a==user and b==password:
        print("login successful")
        return True
    return False
user="chiru"
password="chiru986"
while True:
    if (login()):
        break 