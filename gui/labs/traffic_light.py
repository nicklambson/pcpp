from tkinter import Tk, Button, Canvas

def next():
    global current_phase
    global phase_map
    global back_plate
    if current_phase == 3:
        current_phase = 0
    else:
        current_phase += 1
    phase = phases[current_phase]
    for index, state in enumerate(phase, start=1):
        item_index = index * 2
        back_plate.itemconfig(item_index, state=phase_map[state])

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

phase_map = {True : "normal", False : "hidden"}

current_phase = 0

window = Tk()
back_plate = Canvas(window, background="grey", width=190, height=530)
red_back_plate = back_plate.create_oval(20, 20, 170, 170, outline="black", width=5) # item 1
red_light = back_plate.create_oval(20, 20, 170, 170, fill="red", outline="black", width=5, state="normal") # item 2
yellow_back_plate = back_plate.create_oval(20, 190, 170, 340, outline="black", width=5) # item 3
yellow_light = back_plate.create_oval(20, 190, 170, 340, fill="yellow", outline="black", width=5, state="hidden") # item 4
green_back_plate = back_plate.create_oval(20, 360, 170, 510, outline="black", width=5) # item 5
green_light = back_plate.create_oval(20, 360, 170, 510, fill="green", outline="black", width=5, state="hidden") # item 6
back_plate.pack()

next_button = Button(window, text="Next", command=next)
next_button.pack()
quit_button = Button(window, text="Quit", command=window.destroy)
quit_button.pack()

window.mainloop()
