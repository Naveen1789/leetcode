class Solution(object):
    def isValidInBox(self, board, row1, row2, col1, col2, val):
        if board[row1][col1] == val or board[row1][col2] == val or board[row2][col1] == val or board[row2][col2] == val:
            return False

        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        numOfRows = len(board)
        numOfCols = len(board[0])

        # check if there are duplicates in row
        c = 0
        while c < numOfCols:
            r = 0
            while r < (numOfRows - 1):
                nextRow = r + 1
                while nextRow <  numOfRows:
                    if (board[r][c] != '.') and (board[r][c] == board[nextRow][c]):
                        return False
                    nextRow = nextRow + 1
                r = r + 1
            c = c + 1

        # check if there are duplicates in col
        r = 0
        while r < numOfRows:
            c = 0
            while c < (numOfCols - 1):
                nextCol = c + 1
                while nextCol < numOfCols:
                    if (board[r][c] != '.') and (board[r][c] == board[r][nextCol]):
                        return False
                    nextCol = nextCol + 1
                c = c + 1
            r = r + 1

        # check if there are duplicates in the box (square)
        r = 0
        c = 0
        while r < numOfRows:
            c = 0
            while c < numOfCols:
                if board[r][c] == '.':
                    c = c + 1
                    continue

                if r % 3 == 0:
                    row1 = r + 1
                    row2 = r + 2
                elif r % 3 == 1:
                    row1 = r - 1
                    row2 = r + 1
                else:
                    row1 = r - 1
                    row2 = r - 2

                if c % 3 == 0:
                    col1 = c + 1
                    col2 = c + 2
                elif c % 3 == 1:
                    col1 = c - 1
                    col2 = c + 1
                else:
                    col1 = c - 1
                    col2 = c - 2

                isValid = self.isValidInBox(board, row1, row2, col1, col2, board[r][c])
                if not isValid:
                    return False

                c = c + 1
            r = r + 1


        return True
