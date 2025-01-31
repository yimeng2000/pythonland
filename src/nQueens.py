def nQueens(n):
    queenRow = [-1] * n
    return nQueensSolver(0, queenRow)


def nQueensIsLegal(row, col, queenRow):
    # a position is legal if it's on the board (which we can assume
    # by way of our algorithm) and no prior queen (in a column < col)
    # attacks this position
    for qcol in range(col):
        qrow = queenRow[qcol]
        if (
            (qrow == row)
            or (qcol == col)
            or (qrow + qcol == row + col)
            or (qrow - qcol == row - col)
        ):
            return False
    return True


def nQueensFormatSolution(queenRow):
    # If we have found a solution, format it as a 2D list
    solution = [(["- "] * n) for row in range(n)]
    for col in range(n):
        row = queenRow[col]
        solution[row][col] = "Q "
    return "\n".join(["".join(row) for row in solution])


def nQueensSolver(col, queenRow):
    # Recursive backtracker for nQueens that tries to insert a queen into column
    # col, where queenRow keeps track of the row # of the queen in each column
    if col == n:
        return nQueensFormatSolution(queenRow)
    else:
        # try to place the queen in each row in turn in this col,
        # and then recursively solve the rest of the columns
        for row in range(n):
            if nQueensIsLegal(row, col, queenRow):
                queenRow[col] = row  # place the queen and hope it works
                solution = nQueensSolver(col + 1, queenRow)
                if solution != None:
                    # ta da! it did work
                    return solution
                queenRow[col] = -1  # pick up the wrongly-placed queen
        # shoot, can't place the queen anywhere
        return None


for n in range(1, 10):
    print("n =", n)
    print(nQueens(n))
    print("******************************")
