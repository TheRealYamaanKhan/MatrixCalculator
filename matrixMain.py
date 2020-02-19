import matrixFunctions

inputM = " "
mA = []
mB = []

while (inputM != 'q'):
    inputM = input("Enter a value: ")

    if (inputM == 'a'):  # create matrixA
        matrixFunctions.createMatrix(mA)
        matrixFunctions.rowM1 = matrixFunctions.row
        matrixFunctions.colM1 = matrixFunctions.col

    if (inputM == 'b'):  # create matrixB
        matrixFunctions.createMatrix(mB)
        matrixFunctions.rowM2 = matrixFunctions.row
        matrixFunctions.colM2 = matrixFunctions.col

    if (inputM == 'c'):  # A+B
        matrixFunctions.addition(mA, mB)

    if (inputM == 'd'):  # A-B
        matrixFunctions.subtraction(mA, mB)

    if (inputM == 'e'):  # A*B
        matrixFunctions.multiply(mA, mB)

    if (inputM == 'f'):  # Printing A and B
        matrixFunctions.displayMatrices(mA, mB)
