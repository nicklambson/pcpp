import tkinter as tk
import random
from tkinter import messagebox


def jump(event=None):
    global current_x
    global current_y
    global right_x
    global bottom_y
    global my_button
    global count
    if count < 15:
        new_x = random.randint(0, 436)
        new_y = random.randint(0, 475)
        while current_x < new_x < right_x:
            new_x = random.randint(0, 436)
        while current_y < new_y < bottom_y:
            new_y = random.randint(0, 475)
        my_button.place(x=new_x, y=new_y)
        current_x = new_x
        current_y = new_y
        right_x = current_x + 64
        bottom_y = current_y + 25
        count += 1
    else:
        pass

def win():
    messagebox.showinfo(message="You win!!!!!!!")

count = 0
window = tk.Tk()
window.geometry("500x500")

my_button = tk.Button(window, text="Catch me!", bg="red", fg="white", command=win)
current_x = 0
current_y = 0
right_x = current_x + 64
bottom_y = current_y + 25
# dimensions are 64 x 25
my_button.place(x=current_x, y=current_y)
my_button.bind("<Enter>", jump)

window.mainloop()