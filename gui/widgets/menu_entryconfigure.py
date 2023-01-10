import tkinter as tk


def on_off():
    global accessibility
    # but upon first button press, switches the accessibility to ACTIVE.
    if accessibility == tk.DISABLED:
        accessibility = tk.ACTIVE
    # if it's already ACTIVE, switch it to DISABLED.
    else:
        accessibility = tk.DISABLED
    # 1 is the second item in the sub_menu. (indexed)
    # then, a keyword argument pointing to the modified property.
    sub_menu.entryconfigure(1, state=accessibility)


accessibility = tk.DISABLED
window = tk.Tk()
menu = tk.Menu(window)
window.config(menu=menu)
sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
# initially starts out as disabled
sub_menu.add_command(label="Switch", state=tk.DISABLED)
window.mainloop()
