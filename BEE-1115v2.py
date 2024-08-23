X = 1
Y = 1
while X != 0 and Y != 0:
    tX, tY = input("").split()
    X = int(tX)
    Y = int(tY)

    if X > 0 and Y > 0:
        print("primeiro")
    elif X < 0 and Y > 0:
        print("segundo")
    elif X < 0 and Y < 0:
        print("terceiro")
    elif X > 0 and Y < 0:
        print("quarto")