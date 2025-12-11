📝 To-Do List App (Python + SQLite + Tkinter)

A beginner-friendly and lightweight To-Do List Application built using Python.
It uses SQLite for task storage and Tkinter for a simple GUI.
This project is perfect for learning Python fundamentals like databases, CRUD operations, and user interfaces.

📌 Overview

This project allows users to:

✔ Add new tasks
✔ View all tasks
✔ Delete tasks
✔ Store data permanently using SQLite
✔ Run on Windows, macOS, and Linux

The project is made of two main files:

database.py — Handles database operations

ui.py — Manages the GUI and interacts with the database

📁 Project Structure
TO DO LIST APP/
│── database.py        # Create database, add/edit/delete tasks
│── ui.py              # User Interface (Tkinter)
│── todo.db            # Auto-created SQLite database
│── kivyenv/           # (Optional) Python virtual environment
│── README.md          # Project documentation

🛠️ Technologies Used
Component	Technology
Programming Language	Python 3.10
Database	SQLite
GUI Framework	Tkinter
OS Support	macOS, Windows, Linux
⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/todo-app.git
cd todo-app

2️⃣ Create & activate virtual environment (Recommended)
macOS / Linux
python3 -m venv kivyenv
source kivyenv/bin/activate

Windows
python -m venv kivyenv
kivyenv\Scripts\activate

3️⃣ Run the application

First, ensure the database is created:

python database.py


Then run the UI:

python ui.py

💾 Database Details

The project uses a simple SQLite database named todo.db.

Table structure:
CREATE TABLE tasks(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   task TEXT NOT NULL
);


Supported operations:

INSERT (Add task)

DELETE (Remove task)

UPDATE (Edit task) [optional upgrade]

SELECT (Load all tasks)

🧩 Features Explained
✔ Add Tasks

Enter the task name → press Add Task → saved to database instantly.

✔ Delete Tasks

Select any task from the list → click Delete Task.

✔ View Tasks

Every time the app runs, it loads all tasks automatically.

✔ SQLite Storage

Tasks stay saved even after closing the app.

🧪 Future Enhancements

Here are planned improvements:

Task editing feature

Mark task as completed

Better UI with custom themes

Dark mode

Export tasks to PDF / Excel

Mobile version using Kivy



👨‍💻 Author

Sahil Chauhan
Python Developer | Learning Data Analytics
GitHub: your-profile-link

⭐ Like this project?

If you found it useful, please give it a star ⭐ on GitHub!
