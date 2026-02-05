import tkinter as tk
from tkinter import ttk
from datetime import datetime

# --------------------- Functions ---------------------


def StartTimeNow():

    global Startime
    Startime = datetime.now()  
    start_output_string.set(Startime.strftime("%H:%M"))  


def EndTimeNow():

    global Endtime
    Endtime = datetime.now()
    end_output_string.set(Endtime.strftime("%H:%M"))


def calTotal():

    total = Endtime - Startime  # timedelta
    total_seconds = int(total.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    output_string.set(f"{hours} hrs {minutes} mins")



window = tk.Tk()
window.title('Time Tracker')
window.geometry('400x400')

# Title
title = ttk.Label(window, text='Time Tracker',
                  font=('San Francisco', 25, 'bold'))
title.pack(pady=20)

# Frame for buttons and outputs
frame = tk.Frame(window)
frame.pack(pady=10)

# Start Time Button and Display
startButton = tk.Button(frame, text='Start Time', font=('San Francisco', 15),
                        bg='pink', command=StartTimeNow)
startButton.pack(pady=10)

start_output_string = tk.StringVar()
start_output = tk.Label(frame, font=('San Francisco', 15),
                        textvariable=start_output_string)
start_output.pack()

# End Time Button and Display
endButton = tk.Button(frame, text='End Time', font=('San Francisco', 15),
                      bg='pink', command=EndTimeNow)
endButton.pack(pady=10)

end_output_string = tk.StringVar()
end_output = tk.Label(frame, font=('San Francisco', 15),
                      textvariable=end_output_string)
end_output.pack()

# Total Time Button and Display
totalButton = tk.Button(frame, text='Total Time',
                        font=('San Francisco', 15),
                        bg='pink', command=calTotal)
totalButton.pack(pady=10)

output_string = tk.StringVar()
output = tk.Label(frame, font=('San Francisco', 15),
                  textvariable=output_string)
output.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
