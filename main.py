import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [" "]*9

def check_winner():
	# Check all rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True, board[i]
        
	# Check all columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True, board[i]

	# Check all diagonals
    if board[0] == board[4] == board[8] != " ":
        return True, board[0]
    if board[2] == board[4] == board[6] != " ":
        return True, board[2]
    
    if " " not in board:
        return True, "Tie"
    
    return False, ""
        
def on_button_click(index):
    global current_player
    
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)

        # Check for a winner
        is_winner, winner = check_winner()
        if is_winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_game()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
            
def reset_game():
    global current_player, board
    current_player = "X"
    board = [" "]*9
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)
        
# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", width=10, height=4,
                      command=lambda index=i: on_button_click(index))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create a reset button
reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the main loop
window.mainloop()