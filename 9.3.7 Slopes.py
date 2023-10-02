mylist = []
for i in range(5):
    x = int(input("X Coordinate: "))
    y = int(input("Y Coordinate: "))
    mylist.append((x, y))
    
for i in range(4):
    y1 = mylist[i][1]
    x1 = mylist[i][0]
    y2 = mylist[i + 1][1]
    x2 = mylist[i + 1][0]


    slope = float(y2 - y1) / float(x2 - x1)
    print("Slope between " + str(mylist[i]) + " and " + str(mylist[i + 1]) + ": " + str(slope))
