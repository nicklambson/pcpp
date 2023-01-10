import tkinter
from tkinter import messagebox

# this is an event handler: a piece of code responsible for responding to all clicks addressed to our button

# a function designed to be invoked by someone or something else is often called a callback.

# we will use the names handler and callback interchangeable.
def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()
