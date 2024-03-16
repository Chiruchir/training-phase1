for i in range(8,1,-2):
    for j in range(1,8):
        if j>=i-1:
            print("x",end=" ")
        else:
            print("",end=" ")
    print()