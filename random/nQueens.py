class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = ["."*n for _ in range(n)]
        solutions = []
        self.placeQueen(board, 0, n, solutions)
        return solutions

    def placeQueen(self, board, row, n, solutions):

        # Attempt to place at every position in that row
        for col in range(n):
            b = board.copy()
            if self.canPlace(b, row, col, n):

                # Add queen at that index
                b[row] = b[row][:col] + "Q" + b[row][col+1:]

                # If last row then we add to solutions list
                if row == n - 1:
                    solutions.append(b)

                # Otherwise we look to place at next row
                else:
                    self.placeQueen(b, row + 1, n, solutions)

    # Check if queen can be placed in given spot

    def canPlace(self, board, row, col, n):

        # Ensure no queens in same column
        for i in range(n):
            if board[i][col] == "Q":
                return False

        # Ensure no queens in same row
        for i in range(n):
            if board[row][i] == "Q":
                return False

        # Check negative negative diagonal
        r = row
        c = col
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # Check positive negative diagonal
        r = row
        c = col
        while r < n and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        # Check negative positive diagonal
        r = row
        c = col
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        # Check positive positive diagonal
        r = row
        c = col
        while r < n and c < n:
            if board[r][c] == "Q":
                return False
            r += 1
            c += 1

        return True
