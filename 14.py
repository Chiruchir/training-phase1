for i in range(1,5):
    for j in range(1,5):
        if j==1 or j==4 or i==1 or i==4:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print() 