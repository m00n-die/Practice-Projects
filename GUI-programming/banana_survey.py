"""A simple survey application built with Tkinter in python"""
import tkinter as tk

root = tk.Tk()
root.title("Banana Survey Application")
root.geometry('640x480+300+300')
root.resizable(False, False)
title = tk.Label(root, text="Please take the survey below", 
                 font=('Arial 16 bold'), 
                 bg='brown', 
                 fg='#FF0')

name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What is your name?")
name_inp = tk.Entry(root, textvariable=name_var)
eater_var = tk.BooleanVar(root)
eater_inp = tk.Checkbutton(root, variable=eater_var, text="Check this box if you eat bananas")
num_var = tk.IntVar(value=3)
num_label = tk.Label(root, text="How many bana s do you eat per day?")
num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)
color_var = tk.StringVar(value="Any")
color_label = tk.Label(root, text="what is the best color for a banana?")

color_choices = (
    'Any', 'Green', 'Green-Yellow',
    'Yellow', 'Brown Spotted', 'Black'
)
color_inp = tk.OptionMenu(root, color_var, *color_choices)

plantain_var = tk.BooleanVar()
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame,
                                  text="Yes",
                                  value=True,
                                  variable=plantain_var
)
plantain_no_inp = tk.Radiobutton(plantain_frame,
                                 text="Eww, no!",
                                 value=False,
                                 variable=plantain_var
)

banana_haiku_label = tk.Label(root, text="Write a haiku about bananas")
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text="Submit survey")
output_var = tk.StringVar(value="")
output_line = tk.Label(root, textvariable=output_var, text="", anchor="w", justify="left"
                       )


"""Arranging the widgets"""
title.grid()
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
title.grid(columnspan=2)
eater_inp.grid(row=2, columnspan=2, sticky="we")
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.E + tk.W))
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)
plantain_yes_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, stick=tk.W)
banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

def on_submit():
    """Function that executes when Submit Survey button is clicked"""
    name = name_var.get()
    try:
        number = num_inp.get()
    except tk.TclError:
        number = 1000
    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()
    haiku = banana_haiku_inp.get('1.0', tk.END)

    message = f'Thanks for taking the survey, {name}.\n'
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f'Enjoy your {number} {color} bananas!\n'
    if plantain_eater:
        message += 'Enjoy your plantains!'
    else:
        message += 'May you successfully avoid plantains!'
    if haiku.strip():
        message += f'\n\nYour Haiku:\n{haiku}'

    output_var.set(message)

submit_btn.configure(command=on_submit)

root.mainloop()