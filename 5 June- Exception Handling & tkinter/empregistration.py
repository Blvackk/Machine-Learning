import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- Database Connection ---------------- #

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",      # Change if your MySQL password is different
        database="pythondb"
    )


# ---------------- Load Students ---------------- #

def load_students():
    for row in listBox.get_children():
        listBox.delete(row)

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()

        for row in rows:
            listBox.insert("", tk.END, values=row)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------- Add Student ---------------- #

def add_student():
    name = e2.get()
    course = e3.get()
    fee = e4.get()

    if name == "" or course == "" or fee == "":
        messagebox.showerror("Error", "All fields are required.")
        return

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO student(name, course, fee) VALUES(%s,%s,%s)"
        cursor.execute(sql, (name, course, fee))
        conn.commit()

        messagebox.showinfo("Success", "Student added successfully.")

        clear_entries()
        load_students()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------- Update Student ---------------- #

def update_student():

    if e1.get() == "":
        messagebox.showerror("Error", "Please select a student.")
        return

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE student
        SET name=%s, course=%s, fee=%s
        WHERE id=%s
        """

        cursor.execute(sql, (
            e2.get(),
            e3.get(),
            e4.get(),
            e1.get()
        ))

        conn.commit()

        messagebox.showinfo("Success", "Record updated.")

        clear_entries()
        load_students()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------- Delete Student ---------------- #

def delete_student():

    if e1.get() == "":
        messagebox.showerror("Error", "Please select a student.")
        return

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM student WHERE id=%s", (e1.get(),))
        conn.commit()

        messagebox.showinfo("Success", "Record deleted.")

        clear_entries()
        load_students()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------- Clear Entry Boxes ---------------- #

def clear_entries():
    e1.config(state="normal")

    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)

    e1.config(state="disabled")


# ---------------- Treeview Selection ---------------- #

def on_treeview_select(event):

    selected = listBox.selection()

    if selected:

        values = listBox.item(selected[0])["values"]

        e1.config(state="normal")

        e1.delete(0, tk.END)
        e1.insert(0, values[0])

        e2.delete(0, tk.END)
        e2.insert(0, values[1])

        e3.delete(0, tk.END)
        e3.insert(0, values[2])

        e4.delete(0, tk.END)
        e4.insert(0, values[3])


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Student Registration System")
root.geometry("700x500")

tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=10)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)

tk.Label(root, text="Course").grid(row=2, column=0, padx=10, pady=10)

tk.Label(root, text="Fee").grid(row=3, column=0, padx=10, pady=10)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)
e1.config(state="disabled")

e2 = tk.Entry(root)
e2.grid(row=1, column=1)

e3 = tk.Entry(root)
e3.grid(row=2, column=1)

e4 = tk.Entry(root)
e4.grid(row=3, column=1)

tk.Button(root, text="Add", width=10, command=add_student).grid(row=4, column=0, pady=15)

tk.Button(root, text="Update", width=10, command=update_student).grid(row=4, column=1)

tk.Button(root, text="Delete", width=10, command=delete_student).grid(row=4, column=2)

columns = ("id", "name", "course", "fee")

listBox = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    listBox.heading(col, text=col.capitalize())
    listBox.column(col, width=150)

listBox.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

listBox.bind("<ButtonRelease-1>", on_treeview_select)

load_students()

root.mainloop()