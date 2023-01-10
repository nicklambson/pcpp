import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    # If the switch is on, Button2 does nothing
    # and the text is set to Gee!
    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    # If the switch is off, Button2 displays PEEKABOO!
    # and the button text is set to Peekaboo!
    else:
        # information about a previously used callback is lost
        # you must repeat the bind() or config() function.
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch


def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")


def do_nothing():
    pass


switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()