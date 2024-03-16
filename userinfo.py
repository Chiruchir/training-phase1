import csv
users=[{"username":"chiru","email":"chiru@gmail.com","password":"chiru986"}]
with open("users.csv","w",newline="")as file:
    writer = csv.DictWriter(file, fieldnames=["username", "email", "password"])
    writer.writeheader()
    for user in users:
        writer.writerow(user)