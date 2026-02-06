import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as tb


def username():

    fname = fname_string.get()[0]
    sname = sname_string.get()
    house = house_string.get()[0]
    year = year_string.get()[1]

    username = fname + sname + '_' + house + year

    output_string.set(username)


window = tk.Tk()
window.title('log in')
window.geometry('1000x500')

title = ttk.Label(master=window,
                  text='Log in',
                  font=('San Francisco', 25, 'bold'))
title.pack()

# labels
frame_input = ttk.Frame(master=window)

fname_frame = ttk.Frame(master=frame_input)
fname_string = tk.StringVar()
fname_label = tk.Label(master=fname_frame,
                       text='Forename  ',
                       font=('San Francisco', 15, 'bold'))
fname_entry = ttk.Entry(master=fname_frame,
                        textvariable=fname_string)

fname_label.pack(side='left')
fname_entry.pack(pady=5, padx=5)
fname_frame.pack(pady=10)

sname_frame = ttk.Frame(master=frame_input)
sname_string = tk.StringVar()
sname_label = tk.Label(master=sname_frame,
                       text='Surname  ',
                       font=('San Francisco', 15, 'bold'))
sname_entry = ttk.Entry(master=sname_frame,
                        textvariable=sname_string)

sname_label.pack(side='left')
sname_entry.pack(pady=5, padx=5)
sname_frame.pack(pady=10)

house_frame = ttk.Frame(master=frame_input)
house_string = tk.StringVar()
house_label = tk.Label(master=house_frame,
                       text='House        ',
                       font=('San Francisco', 15, 'bold'))
house_entry = ttk.Entry(master=house_frame,
                        textvariable=house_string)

house_label.pack(side='left')
house_entry.pack(pady=5, padx=5)
house_frame.pack(pady=10)


year_frame = ttk.Frame(master=frame_input)
year_string = tk.StringVar()
year_label = tk.Label(master=year_frame,
                      text='Year Group',
                      font=('San Francisco', 15, 'bold'))
year_entry = ttk.Entry(master=year_frame,
                       textvariable=year_string)

year_label.pack(side='left')
year_entry.pack(pady=5, padx=5)
year_frame.pack(pady=10)

button = ttk.Button(master=frame_input,
                    text='convert',
                    command=username)

button.pack(side='left')


frame_input.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font=('Arial', 25),
                         textvariable=output_string
                         )

output_label.pack(pady=5)
# run
window.mainloop()
