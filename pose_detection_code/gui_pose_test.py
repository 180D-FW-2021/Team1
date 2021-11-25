#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('800x600')

header = tk.Frame(root, bg='#8ecae6') #8ecae6
content = tk.Frame(root, bg='white')
footer = tk.Frame(root, bg='white')

root.columnconfigure(0, weight=1) # 100% 

root.rowconfigure(0, weight=1) # 20%
root.rowconfigure(1, weight=8) # 70%
root.rowconfigure(2, weight=1) # 10%

header.grid(row=0, sticky='news')
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

text = tk.Label(root, text="AirController", bg='#8ecae6', font=("Helvetica", 18)).place(relx=0.5,rely=0.05,anchor='center')

tutorial_button = tk.Button(root, text="Show Tutorial", activebackground='#517687', activeforeground='black', bg='#8ecae6', width=25, font=("Helvetica", 14)).place(x=30, rely=0.2, anchor='w')

customize_button = tk.Button(root, text="Customize Gestures", activebackground='#517687', activeforeground='black', bg='#8ecae6', width=25, font=("Helvetica", 14)).place(x=770, rely=0.2, anchor='e')

display_gestures_button = tk.Button(root, text="Display Gestures", activebackground='#517687', activeforeground='black', bg='#8ecae6', width=25, font=("Helvetica", 14)).place(x=30, rely=0.35, anchor='w')

root.mainloop()