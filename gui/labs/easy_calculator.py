import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None

def string_to_int_or_float(my_string):
    try:
        return int(my_string)
    except ValueError:
        try:
            return float(my_string)
        except ValueError:
            return None

def evaluate():
    global entry_1_var
    global entry_2_var
    x = string_to_int_or_float(entry_1_var.get())
    y = string_to_int_or_float(entry_2_var.get())
    if x is None:
        messagebox.showerror(message=f"Field one is not a valid number: {entry_1_var.get()}")
        entry_1.focus_set()
    elif y is None:
        messagebox.showerror(message=f"Field two is not a valid number: {entry_2_var.get()}")
        entry_2.focus_set()
    else:
        operation = radio_1_var.get()
        result = operations_dict[operation](x, y)
        if result is None:
            messagebox.showerror(message=f"Cannot divide by zero.")
            entry_2.focus_set()
        else:
            messagebox.showinfo(message=result)


operations_dict = {1 : add, 2 : subtract, 3 : multiply, 4 : divide}

window = tk.Tk()
window.title("Calculator")

entry_1_var = tk.StringVar()
entry_1 = tk.Entry(window, textvariable=entry_1_var)
entry_1.grid(column=0, row=1)

entry_2_var = tk.StringVar()
entry_2 = tk.Entry(window, textvariable=entry_2_var)
entry_2.grid(column=2, row=1)

radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="+", variable=radio_1_var, value=1)
radio_1_1.select()
radio_1_1.grid(column=1, row=0)
radio_1_2 = tk.Radiobutton(window, text="-", variable=radio_1_var, value=2)
radio_1_2.grid(column=1, row=1)
radio_1_3 = tk.Radiobutton(window, text="*", variable=radio_1_var, value=3)
radio_1_3.grid(column=1, row=2)
radio_1_4 = tk.Radiobutton(window, text="/", variable=radio_1_var, value=4)
radio_1_4.grid(column=1, row=3)

evaluate_button = tk.Button(window, text="Evaluate", command=evaluate)
evaluate_button.grid(column=1, row=4)

window.mainloop()