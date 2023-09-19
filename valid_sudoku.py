def isValidSudoku(board):
    seen = set()
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                # Check row
                if (num, 'in row', i) in seen:
                    return False
                seen.add((num, 'in row', i))

                # Check column
                if (num, 'in col', j) in seen:
                    return False
                seen.add((num, 'in col', j))

                # Check box
                box_id = (i // 3, j // 3)  # Identify which 3x3 box the element belongs to
                if (num, 'in box', box_id) in seen:
                    return False
                seen.add((num, 'in box', box_id))

    return True


def test_isValidSudoku():
    # Test Case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert isValidSudoku(board1) == True, "Test Case 1 Failed"

    # Test Case 2: Invalid Sudoku because of repeated '8' in the first column
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        ["1","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert isValidSudoku(board2) == False, "Test Case 2 Failed"

    # Test Case 3: Invalid Sudoku because of repeated '5' in the bottom-right 3x3 box
    board3 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","5","5"]
    ]
    assert isValidSudoku(board3) == False, "Test Case 3 Failed"

    print("All test cases passed!")


# Run the tests
test_isValidSudoku()
