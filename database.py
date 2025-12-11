import sqlite3

def connect_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task TEXT NOT NULL 
        )
    """)
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def delete_task(task):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
    conn.commit()
    conn.close()

def edit_task(old_task, new_task):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task=? WHERE task=?", (new_task, old_task))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM tasks")
    tasks = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tasks