import tkinter as tk 

def reset_game():
    global win
    win = False

    for col in range(3):
        for row in range(3):
            buttons[col][row].config(text="")

    global current_player
    current_player = "X"

def print_winner():
    global win

    if win is False:
        win = True
        print(f"{current_player} Winner")
        reset_button = tk.Button(root, text="Reset", font=("Arial", 50),relief="groove", width=5, height=1, command=reset_game)
        reset_button.grid(row=3, column=1)



def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_tie():
    for col in range(3):
        for row in range(3):
            if buttons[col][row]["text"] == "":
                return False
    return True

def check_winner(clicked_row, clicked_col):
    # Check column
    count = 0
    for row in range(3):
        if buttons[clicked_col][row]["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # Check row
    count = 0
    for col in range(3):
        if buttons[col][clicked_row]["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # Check diagonal
    count = 0
    for i in range(3):
        if buttons[i][i]["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    count = 0
    for i in range(3):
        if buttons[i][2-i]["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if win is False and check_tie():
        print("Tie")

def place_sign(row, col):
    if buttons[col][row]["text"] == "":
        clicked_button = buttons[col][row]
        clicked_button.config(text=current_player)

        check_winner(row, col)
        check_tie()
        switch_player()

def draw_grid():
    for col in range(3):
        buttons_col = []
        for row in range(3):
            button = tk.Button(root, font=("Arial", 50),relief="groove", width=5, height=3, command=lambda r=row, c=col: place_sign(r, c))
            button.grid(row=row, column=col)
            buttons_col.append(button)
        buttons.append(buttons_col)

#Stockages des valeurs des cases
buttons = []
current_player = "X"
win = False

#Creer la fenetre du jeu
root = tk.Tk()

#Personnalisation de la fenetre
root.title("Tic Tac Toe")
root.minsize(500,500)

draw_grid()

root.mainloop()
