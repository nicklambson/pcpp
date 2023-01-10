import tkinter as tk

# image needs to be an instance of PhotoImage class

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
my_image_path = r"C:\Users\Nick\Documents\GitHub\pcpp\gui\canvas\pcpp.png"
image = tk.PhotoImage(file=my_image_path)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
