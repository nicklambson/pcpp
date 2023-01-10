import tkinter as tk
from tkinter import messagebox


# you can bind a callback to any events that a widget receives. This is done with
# widget.bind(event, callback)
# event is the event you want to launch your callback with;
# callback is the callback itself.

# examples of events are
# <Button-1>
# <Enter> when the mouse cursor appears over the widget
# There are many interesting events!

# a callback designed for usage with the command property is a *paramaterless function*
# a callback intended to cooperate with the bind() method is a one-parameter function. The callback's argument carries some info about the captured event.
# to use a callback with command and with bind, define ev=None as an optional parameter.


# event.x is the x position of the mouse
# event.y is the y position of the mouse
# event.num is the number of the clicked mouse button
# event.type is the event's type

def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)        


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()

