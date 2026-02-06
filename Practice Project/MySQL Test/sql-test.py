
import mysql.connector

import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk
from datetime import datetime
from tkinter import messagebox

# database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    database='new'
)

mycursor = conn.cursor()

# Create table if it doesn't exist
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        startSession VARCHAR(255),
        endSession VARCHAR(255),
        totalHours INT,
        totalMinutes INT,
        totalTime INT
    )
''')
conn.commit()

startTime = datetime.now()
endTime = datetime.now()


def start_insert_data():
    global startTime
    global startTimeStr

    startTime = datetime.now()
    startTimeStr = datetime.now().strftime("%H:%M")
    start_output_string.set("Time logged!")


def end_insert_data():
    global endTime
    global startTimeStr
    global endTimeStr

    endTime = datetime.now()
    endTimeStr = datetime.now().strftime("%H:%M")

    end_output_string.set("Time logged!")


def getTimeNow():
    return datetime.now().strftime("%H:%M")


# Calculates the total session time in seconds

def calTotal():
    total = endTime - startTime
    total_seconds = int(total.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    output_string.set(f"{hours} hrs {minutes} mins")

    sql = "INSERT INTO sessions (startSession, endSession, totalHours, totalMinutes) VALUES (%s,%s,%s,%s)"
    # Flat tuple with both values
    values = (startTimeStr, endTimeStr, hours, minutes)

    mycursor.execute(sql, values)
    conn.commit()


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
                        command=start_insert_data)


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
                      command=end_insert_data)


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
