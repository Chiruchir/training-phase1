import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentId","rollno","name","phoneno"])
id=int(input("enter id:"))
rollno=int(input("enter rollno:"))
name=input("enter name:")
phoneno=int(input("enter phoneno:"))
a.writerow([id,rollno,name,phoneno])
print("student record saved")