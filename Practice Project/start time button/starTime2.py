import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk
from datetime import datetime


def StartTimeNow():
    global Startime
    Startime = datetime.now()
    start_string.set(Startime.strftime("%H:%M"))


def EndTimeNow():
    global Endtime
    Endtime = datetime.now()
    end_string.set(Endtime.strftime("%H:%M"))


def calTotal():
    total = Endtime - Startime
    total_seconds = int(total.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    output_string.set(f"{hours} hrs {minutes} mins")


# window
window = tk.Tk()

window.title('time')
window.geometry('500x600')

title = ttk.Label(master=window,
                  text='time tracker',
                  font=('San Francisco', 25, 'bold'))
title.pack()

frame = tk.Frame(master=window)
startButton = tk.Button(master=frame,
                        text='start Time',
                        font=('San Francisco', 15),
                        bg='pink',
                        command=StartTimeNow)


start_string = tk.StringVar()
start_output = tk.Label(master=frame,
                        text=' ',
                        font=('San Francisco', 15),
                        textvariable=start_string)

endButton = tk.Button(master=frame,
                      text='end Time',
                      font=('San Francisco', 15),
                      bg='pink',
                      command=EndTimeNow)


end_string = tk.StringVar()
end_output = tk.Label(master=frame,
                      text=' ',
                      font=('San Francisco', 15),
                      textvariable=end_string)

output_string = tk.StringVar()
output = tk.Label(master=frame,
                  text='total hrs',
                  font=('San Francisco', 15),
                  textvariable=output_string)

totalButton = tk.Button(master=frame,
                        text='total Time',
                        font=('San Francisco', 15),
                        bg='pink',
                        command=calTotal)

startButton.pack(pady=50)
start_output.pack()

endButton.pack(pady=50)
end_output.pack()

totalButton.pack(pady=50)
output.pack()

frame.pack()

window.mainloop()

# window
