import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="pirate", cursor="pirate")
label_1.pack()
label_2 = tk.Label(window, height=3, text="man", cursor="man")
label_2.pack()
label_3 = tk.Label(window, height=3, text="fleur", cursor="fleur")
label_3.pack()
window.mainloop()