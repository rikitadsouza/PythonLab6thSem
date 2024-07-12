print("water Jug Problem")
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

while True:
    rno = int(input("Enter rule no: "))
    
    if rno == 1:
        if x < 4:
            x = 4
    elif rno == 2:
        if y < 3:
            y = 3
    elif rno == 3:
        if x > 0:
            x = 0
    elif rno == 4:
        if y > 0:
            y = 0
    elif rno == 5:
        if x + y >= 4 and y > 0:
            x, y = 4, y - (4 - x)
    elif rno == 6:
        if x + y <= 3 and x > 0:
            x, y = x - (3 - y), 3
    elif rno == 7:
        if x + y <= 4 and y > 0:
            x, y = x + y, 0
    elif rno == 8:
        if x + y <= 3 and x > 0:
            x, y = 0, x + y
    
    print("X =", x)
    print("Y =", y)
    
    if x == 2 and y == 0:
        print("goal state")
        break