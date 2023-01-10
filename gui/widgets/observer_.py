# Each observable variable can be enriched with a number of observers. An observer is a function (a kind of callback) which will be invoked automatically each time a specified event occurs in the variable’s life.

# "r" triggers when read
# "w" triggers when written to
# "u" triggers when deleted

import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)
variable.set(variable.get() + 'e') # r observer has been deleted, so only "Writing" is observed
variable.trace_vdelete("w", w_obsid)
variable.set(variable.get() + 'f') # w and r observers have both been deleted.
print(variable.get())
