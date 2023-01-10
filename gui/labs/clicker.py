import tkinter as tk
import random

def increment_timer():
    global timer
    global timer_running
    if len(existing_numbers) == 0:
        timer_running = False
        return
    else:
        timer_running = True
        timer.set(timer.get() + 1)
        window.after(1000, increment_timer)

def click(event: tk.Event):
    if timer_running is False:
        increment_timer()
    my_button = event.widget
    button_value = my_button["text"]
    if button_value == min(existing_numbers):
        existing_numbers.remove(button_value)
        my_button.config(state=tk.DISABLED)
        my_button.unbind("<Button-1>")
    
timer_running = False
window = tk.Tk()
existing_numbers = list()

for i in range(25):
    button_text = random.randint(1,25)
    while button_text in existing_numbers:
        button_text = random.randint(1,25)
    existing_numbers.append(button_text)
    my_button = tk.Button(window, text=button_text, width=10)
    my_button.bind("<Button-1>", click)
    x, y = divmod(i, 5)
    my_button.grid(column=x, row=y)

timer = tk.IntVar()
timer_label = tk.Label(window, textvariable=timer)
timer_label.grid(column=0, row=5, columnspan=5)

window.mainloop()