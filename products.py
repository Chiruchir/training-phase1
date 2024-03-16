import csv
class products:
    def add(chiru,n,m,q):
        chiru.n=n
        chiru.m=m
        chiru.q=q
        with open("store.csv","a",newline="") as file:
            a=csv.writer(file)
            a.writerow([chiru.n,chiru.m,chiru.q])
        