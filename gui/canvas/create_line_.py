import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# draws a line, each pair is x, y (from top left)
canvas.create_line(10, 350,
                   200, 10,
                   380, 380,
                   10, 380,
                   190, 250,
                   arrow=tk.BOTH, fill='red', smooth=False, width=3)

canvas.create_line(180, 240,
                   190, 160,
                   30, 30,
                   50, 390,
                   390, 10,
                   arrow=tk.BOTH, fill='blue', smooth=True, width=8)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
