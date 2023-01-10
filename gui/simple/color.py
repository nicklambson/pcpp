import tkinter as tk

# background and foreground manage color when un-pressed
# activebackground and activeforeground manage color when pressed

window = tk.Tk()

button = tk.Button(window, text="Button #1",
                   bg="MediumPurple",
                   fg="LightSalmon",
                   activeforeground="LavenderBlush",
                   activebackground="HotPink")
button.pack()

button2 = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")

button2.pack()

window.mainloop()
