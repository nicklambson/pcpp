import tkinter as tk


def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))


counter = 10
window = tk.Tk()
window.title(str(counter))
window.bind("<Button-1>", click)

# set up an image as the icon
my_image_path = r"C:\Users\Nick\Documents\GitHub\pcpp\gui\widgets\pcpp.png"
# this is a low-level communication with the OS's window manager
# asking it to replace the window's icon with a new one.
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file=my_image_path))
window.bind("&lt;Button-1&gt;", lambda e: window.destroy())

window.mainloop()





