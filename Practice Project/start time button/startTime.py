import mysql.connector

import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk
from datetime import datetime

# database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    database='new'
)

mycursor = conn.cursor()

# Created table

start_time = datetime.now()
end_time = datetime.now()


def StartTimeNow():
    start_time = datetime.now()
    start_output_string.set(getTimeNow())


def EndTimeNow():
    end_time = datetime.now()
    end_output_string.set(getTimeNow())


def getTimeNow():
    return datetime.now().strftime("%H:%M")


def insert(Session):
    sess = start_output_string.get()

    sqlFormula = 'INSERT INTO session (endSession) VALUE (%s)'
    mycursor.execute(sqlFormula, (sess))


# Calculates the total session time in seconds

def calTotal():
    total = end_time - start_time
    total_seconds = int(total.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    output_string.set(f"{hours} hrs {minutes} mins")


# window
window = tk.Tk()

window.title('time')
window.geometry('500x500')

title = ttk.Label(master=window,
                  text='time tracker',
                  font=('San Francisco', 25, 'bold'))
title.pack()

frame = tk.Frame(master=window)
# start button
startButton = tk.Button(master=frame,
                        text='start Time',
                        font=('San Francisco', 15),
                        bg='pink',
                        command=StartTimeNow)


start_output_string = tk.StringVar()
start_output = tk.Label(master=frame,
                        text=' ',
                        font=('San Francisco', 15),
                        textvariable=start_output_string)

# end button
endButton = tk.Button(master=frame,
                      text='end Time',
                      font=('San Francisco', 15),
                      bg='pink',
                      command=EndTimeNow)


end_output_string = tk.StringVar()
end_output = tk.Label(master=frame,
                      text=' ',
                      font=('San Francisco', 15),
                      textvariable=end_output_string)

output_string = tk.StringVar()
output = tk.Label(master=frame,
                  text='total hrs',
                  font=('San Francisco', 15),
                  textvariable=output_string)

# total button
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

conn.commit()
