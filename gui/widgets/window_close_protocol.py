import tkinter as tk
from tkinter import messagebox


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


window = tk.Tk()
# binds a custom command to the red X close button
window.protocol("WM_DELETE_WINDOW", really)
window.mainloop()
