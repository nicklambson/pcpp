import tkinter as tk

# every widget has a dictionary containing its properties.
# You can set it like this:

# old_val = Widget["prop"]
# Widget["prop"] = new_val

def on_off_1():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state

# You can also access and modify the properties using .cget()
# and config()

# old_val = Widget.cget("prop")
# Widget.config(prop=new_val)

def on_off_2():
    global button
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button.config(text=state)


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off_2)
button.place(x=50, y=100, width=100)
window.mainloop()
