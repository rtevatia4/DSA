# input1: XO..XX..O
import math

class TicTacToe:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.n = int(math.sqrt(len(matrix_string)))
        self.matrix = [matrix_string[i:i+self.n] for i in range(0, len(matrix_string), self.n)]

    def check_rows(self):
        for row in self.matrix:
            if all(cell == 'X' for cell in row):
                return 'X'
            elif all(cell == 'O' for cell in row):
                return 'O'
        return None

    def check_columns(self):
        for col in range(self.n):
            if all(self.matrix[row][col] == 'X' for row in range(self.n)):
                return 'X'
            elif all(self.matrix[row][col] == 'O' for row in range(self.n)):
                return 'O'
        return None
   
    def check_diagonals(self):
        if all(self.matrix[i][i] == 'X' for i in range(self.n)):
            return 'X'
        elif all(self.matrix[i][i] == 'O' for i in range(self.n)):
            return 'O'

        if all(self.matrix[i][self.n - i - 1] == 'X' for i in range(self.n)):
            return 'X'
        elif all(self.matrix[i][self.n - i - 1] == 'O' for i in range(self.n)):
            return 'O'

        return None
   
    def check_winner(self):

        winner = self.check_rows() or self.check_columns() or self.check_diagonals()
        return winner if winner else "No winner"

# Example usage:
matrix_string = "XOXXOXOO."
game = TicTacToe(matrix_string)
winner = game.check_winner()
print(f"The winner is: {winner}")