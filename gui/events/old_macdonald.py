import tkinter as tk


def on_off():
    global switch
    # unbind it if switch is on.
    if switch:
        label.unbind("<Button-1>")
    # rebind it if swich is off
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch


def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])


switch = True
#         0          1       2      3     4
#         5          6       7      8     9
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off)
button.pack()
label = tk.Label(window, text=words[0])

# When you click the button, it will activate the rhyme callback
label.bind("<Button-1>", rhyme)
label.pack()
window.mainloop()
