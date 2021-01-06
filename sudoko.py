def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not not filled yet --> rep with -1
    #return row, col tuple (or (None, None) of there is none)

    #we are using 0-8 indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  #if no spaces left in the puzzle

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at row/col of the puzzle is a valid guess
    #returns True if is valid, False otherwise

    #let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False


    #and then the square
    #we want to get where the 3x3 matrix starts
    #and iterate over the 3 values in row/column
    row_start = (row//3) * 3 # 1//3 = 0, 5//3 = 1, ...
    col_start = (col//3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_Sudoko(puzzle):
    #solve sudoko using backtracking
    #our puzzle is a list of lists, where inner list is row in our puzzle
    #return whether solution exists
    #mutates puzzle to be a solution (if solution exists)

    #choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1: if there's nowhere left, then we are done because we only allowed valid inputs
    if row is None:
        return True

    #step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        #step 3: check if valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse the puzzle
            # step 4: recursivley call our function
            if solve_Sudoko(puzzle):
                return True

        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if none of the numbers work, then the puzzle in UNSOLVABLE
    return False

if __name__ == '__main__':
    example_board = [
        [-1, -1, -1,   2, 6, -1,   7, -1, 1],
        [6, 8, -1,   -1, 7, -1,   -1, 9, -1],
        [1, 9, -1,   -1, -1, 4,   5, -1, -1],

        [8, 2, -1,   1, -1,-1,   -1, 4, -1],
        [-1, -1, 4,   6, -1, 2,   9, -1, -1],
        [-1, 5, -1,   -1, -1, 3,   -1, 2, 8],

        [-1, -1, 9,   3, -1, -1,   -1, 7, 4],
        [-1, 4, -1,   -1, 5, -1,   -1, 3, 6],
        [7, -1, 3,   -1, 1, 8,   -1, -1, -1]
    ]
    print(solve_Sudoko(example_board))
    print(example_board)
