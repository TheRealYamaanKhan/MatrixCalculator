import matrixErrors

M1 = []
M2 = []
row = 0
global rowM1
global rowM2
col = 0
global colM1
global colM2

# row by column


def createMatrix(newM):

    global row
    global col

    newM.clear()

    try:
        row = int(input("Enter number of rows: "))
        col = int(input("Enter number of columns: "))
    except TypeError:
        print("Please enter a positive integer!")
    except matrixErrors.NegZeroIntError:  # FIX
        print("Gamer town")

    for x in range(row):
        newM.append([0] * col)

    for x in range(row):
        for y in range(col):
            try:
                val = int(input("Enter a number: "))
                newM[x][y] = val
            except TypeError:
                print("Please enter a rational number!")

    for x in range(row):
        print(newM[x])


def addition(M1, M2):

    addM = []

    # checks to see if the dimensions of both matrices are identical
    if (rowM1 != rowM2):
        print("Matrices have different number of rows!")
        return
    elif (colM1 != colM2):
        print("Matrices have different number of columns!")
        return
    # addition of 2 matrices
    for x in range(row):
        n = []
        for y in range(col):
            n.append(M1[x][y] + M2[x][y])
        addM.append(n)

    for x in range(row):
        print(addM[x])


def subtraction(M1, M2):

    subM = []

    # checks to see if the dimensions of both matrices are identical
    if (rowM1 != rowM2):
        print("Matrices have different number of rows!")
        return
    elif (colM1 != colM2):
        print("Matrices have different number of columns!")
        return

    # subtraction of 2 matrices
    for x in range(row):
        n = []
        for y in range(col):
            n.append(M1[x][y] - M2[x][y])
        subM.append(n)

    for x in range(row):
        print(subM[x])


def multiply(M1, M2):

    multM = []

    # checks to see if the number of columns matches number of rows
    if (colM1 != rowM2):
        print(
            "Number of columns in first matrix must equal number of rows in second matrix!")
        return

    # calculations to create the dimensions for rowM1 by colM2
    for z in range(rowM1):
        b = []
        for x in range(colM2):
            n = []
            m = []
            newCol = [row[x] for row in M2]
            for y in range(rowM2):
                n.append(M1[z][y] * newCol[y])

            # combining the values from list n and combining them into one value to add to the main matrix
            m = n
            for w in range(1, rowM2):
                n[0] = n[0] + m[w]
            b.append(n[0])
        multM.append(b)

    for x in range(rowM1):
        print(multM[x])


def invert(M):
    print("Implement later")

# if matrix A has fewer rows than matrix B, print out multiple spaces for number of columns in matrix A spot


def displayMatrices(M1, M2):

    print("Matrix A --------- Matrix B")

    if (rowM1 > rowM2):
        for x in range(rowM2):
            print(M1[x], "---------", M2[x])
        for y in range(rowM2, rowM1):
            print(M1[y])
    elif (rowM1 < rowM2):
        for x in range(rowM1):
            print(M1[x], "---------", M2[x])
        for y in range(rowM1, rowM2):
            print("---------", M2[y])
    else:
        for x in range(rowM1):
            print(M1[x], "---------", M2[x])


def swapMatrices(M1, M2):
    print("Implement later")
