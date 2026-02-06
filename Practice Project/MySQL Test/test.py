
import tkinter as tk
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    database='new'
)


cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    )
''')
conn.commit()


def insert_data(name_entry, age_entry):
    name = name_entry.get()
    age = age_entry.get()

    sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
    values = (name, age)

    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Data inserted successfully")

    # clear inputs
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


def create_submit_button(parent, name_entry, age_entry):
    btn = tk.Button(
        parent,
        text="Submit",
        command=lambda: insert_data(name_entry, age_entry)
    )
    btn.pack(pady=10)


root = tk.Tk()
root.title("Tkinter + MySQL")
root.geometry("300x200")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

create_submit_button(root, name_entry, age_entry)

root.mainloop()
