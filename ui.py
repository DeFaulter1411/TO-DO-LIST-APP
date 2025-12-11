import tkinter as tk
from tkinter import messagebox
import database

database.connect_db()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")


def load_task():
    task_list.delete(0, tk.END)
    tasks = database.get_tasks()
    for task in tasks:
        task_list.insert(tk.END, task)

def add_new_task():
    task = task_entry.get()
    if task:
        database.add_task(task)
        task_entry.delete(0, tk.END)
        load_task()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")


def delete_selected_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        database.delete_task(selected_task)
        load_task()
    except tk.TclError:
        messagebox.showwarning("Warning", "Please select a task to delete")


def edit_selected_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        new_task = task_entry.get()
        if new_task:
            database.edit_task(selected_task, new_task)
            task_entry.delete(0, tk.END)
            load_task()
        else:
            messagebox.showwarning("Warning", "Enter a new task name!")
    except:
        messagebox.showwarning("Warning", "Please select a task to edit")


# UI Components
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_new_task)
add_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_selected_task)
edit_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_selected_task)
delete_button.pack()

task_list = tk.Listbox(root, width=40, height=15)
task_list.pack(pady=10)

load_task()

root.mainloop()
