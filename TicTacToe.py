import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}  # Score tracking
        self.create_window()

    def create_window(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Status label to display current turn
        self.status_label = tk.Label(self.window, text="Player X's Turn", font=("Arial", 14, "bold"))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Score label
        self.score_label = tk.Label(self.window, text=f"X: {self.scores['X']} | O: {self.scores['O']}", font=("Arial", 12, "bold"))
        self.score_label.grid(row=1, column=0, columnspan=3, pady=5)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", width=10, height=3, font=("Arial", 16, "bold"),
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i + 2, column=j)  # Adjust row index to fit labels
                row.append(button)
            self.buttons.append(row)

        # Restart button
        self.restart_button = tk.Button(self.window, text="Restart", font=("Arial", 12, "bold"),
                                        command=self.restart_game)
        self.restart_button.grid(row=5, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            if self.check_winner(self.current_player):
                self.scores[self.current_player] += 1  # Update score
                self.update_score_label()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.ask_continue_or_exit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.ask_continue_or_exit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check rows
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check columns
                return True

        if all(self.board[i][i] == player for i in range(3)):  # Check main diagonal
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Check secondary diagonal
            return True
        
        return False

    def is_board_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.config(text="Player X's Turn")

        for row in self.buttons:
            for button in row:
                button.config(text=" ", state=tk.NORMAL)

    def update_score_label(self):
        self.score_label.config(text=f"X: {self.scores['X']} | O: {self.scores['O']}")

    def ask_continue_or_exit(self):
        response = messagebox.askquestion("Continue?", "Do you want to play again?")
        if response == "yes":
            self.reset_board()
        else:
            messagebox.showinfo("Final Scores", f"Final Score:\nPlayer X: {self.scores['X']} | Player O: {self.scores['O']}")
            self.scores = {"X": 0, "O": 0}  # Reset scores to 0
            self.window.quit()

    def restart_game(self):
        self.scores = {"X": 0, "O": 0}  # Reset scores to 0 when restarting
        self.update_score_label()
        self.reset_board()

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
