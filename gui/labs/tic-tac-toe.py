import tkinter as tk
from tkinter import messagebox
from random import randrange
import numpy as np


def is_winner(token):
    global rows
    global window
    columns = np.transpose(rows)
    diagonal_1 = [rows[0][0], rows[1][1], rows[2][2]]
    diagonal_2 = [rows[2][0], rows[1][1], rows[0][2]]
    diagonals = [diagonal_1, diagonal_2]
    conditions = list()
    for several_conditions in (rows, columns, diagonals):
        conditions.extend(several_conditions)
    for condition in conditions:
        values = [x["text"] for x in condition]
        if all([x == token for x in values]):
            window.unbind_all("<Button-1>")
            messagebox.showinfo(message="Winner!")
            return True
    else:
        return False

def cpu_move(i=None, j=None):
    global rows
    if i is None and j is None:
        i = randrange(0,3)
        j = randrange(0,3)
        while rows[i][j]["text"] != "":
            i = randrange(0,3)
            j = randrange(0,3)
    rows[i][j]["text"] = "X"
    rows[i][j]["foreground"] = "red"
    result = is_winner("X")

def player_move(event: tk.Event):
    my_button = event.widget
    i = my_button.grid_info()["row"]
    j = my_button.grid_info()["column"]
    rows[i][j]["text"] = "O"
    my_button["foreground"] = "green"
    my_button.unbind("<Button-1>")
    result = is_winner("O")
    if result is False:
        cpu_move()

rows = list()

window = tk.Tk()
window.title("TicTacToe")

for i in range(3):
    my_row = list()
    for j in range(3):
        my_button = tk.Button(window, height=5, width=20)
        my_button.grid(row=i, column=j)
        my_button.bind("<Button-1>", player_move)
        my_row.append(my_button)
    rows.append(my_row)

cpu_move(i=1, j=1)
        
window.mainloop()