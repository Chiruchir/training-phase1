import csv
class landr:
    def userlogin(chiru,u,p):
        with open("userinfo.csv","r",newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row['username']==u and row['password']==p:
                    return True
            return False
    def registration(chiru,username,password,email):
        chiru.uname=username
        chiru.pwd=password
        chiru.em=email
        with open("userinfo.csv","a",newline="") as file:
            a=csv.writer(file)
            a.writerow([chiru.uname,chiru.pwd,chiru.em])