for row in range(8):
    for col in range(9):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
