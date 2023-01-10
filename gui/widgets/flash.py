import tkinter as tk


def switch():
    if button_1.cget('state') == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)


def mouseover(ev):
    button_1['bg'] = 'green'


def mouseout(ev):
    button_1['bg'] = 'red'

def checkbutton_switch():
    button_1['bg'] = 'black'
    print(checkbox_value.get())


window = tk.Tk()
button_1 = tk.Button(window, text="Enabled", bg="red")
button_1.bind("<Enter>", mouseover)
button_1.bind("<Leave>", mouseout)
button_1.pack()
button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()
checkbox_value = tk.BooleanVar(window, value=False)
button_3 = tk.Checkbutton(window, text="I'm a checkbutton.", variable=checkbox_value, offvalue=False, onvalue=True, command=checkbutton_switch)
button_3.pack()

window.mainloop()