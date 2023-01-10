import tkinter as tk
from PIL import ImageTk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='red')
my_image_path = r"C:\Users\Nick\Documents\GitHub\pcpp\gui\canvas\pcpp.jpg"
jpg = ImageTk.PhotoImage(file=my_image_path)
canvas.create_image(200, 200, image=jpg)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
