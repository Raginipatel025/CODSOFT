import tkinter as tk
from tkinter import messagebox, simpledialog

# ------------------ Functions ------------------

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, f"❌ {task}")  # By default task = pending
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def mark_done():
    try:
        selected = listbox.curselection()
        task = listbox.get(selected)
        if task.startswith("❌"):
            listbox.delete(selected)
            listbox.insert(selected, f"✔️ {task[2:]}")
        else:
            messagebox.showinfo("Info", "Task is already completed!")
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def update_task():
    try:
        selected = listbox.curselection()
        old_task = listbox.get(selected)
        new_task = simpledialog.askstring("Update Task", "Edit your task:", initialvalue=old_task[2:])
        if new_task:
            status = "❌" if old_task.startswith("❌") else "✔️"
            listbox.delete(selected)
            listbox.insert(selected, f"{status} {new_task}")
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def view_tasks():
    total = listbox.size()
    if total == 0:
        messagebox.showinfo("Your Tasks", "No tasks found!")
        return
    
    tasks_text = "📋 Your Tasks:\n\n"
    for i in range(total):
        tasks_text += f"{i+1}. {listbox.get(i)}\n"
    messagebox.showinfo("Task List", tasks_text)

def show_summary():
    total = listbox.size()
    done = sum(1 for i in range(total) if listbox.get(i).startswith("✔️"))
    pending = total - done
    messagebox.showinfo("Task Summary", f"📌 Total: {total}\n✅ Done: {done}\n❌ Pending: {pending}")

# ------------------ GUI Setup ------------------

app = tk.Tk()
app.title("✨To-Do List✨")
app.geometry("450x500")
app.config(bg="#f0f8ff")

# Title Label
title = tk.Label(app, text="My To-Do List 📝", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Task Entry
task_entry = tk.Entry(app, width=40, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons Frame
frame = tk.Frame(app, bg="#f0f8ff")
frame.pack(pady=5)

btn_style = {"width": 14, "font": ("Arial", 10), "bg": "#4caf50", "fg": "white"}

add_btn = tk.Button(frame, text="➕ Add Task", command=add_task, **btn_style)
add_btn.grid(row=0, column=0, padx=5, pady=5)

update_btn = tk.Button(frame, text="✏️ Update Task", command=update_task, **btn_style)
update_btn.grid(row=0, column=1, padx=5, pady=5)

delete_btn = tk.Button(frame, text="🗑️ Delete Task", command=delete_task, **btn_style)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

mark_btn = tk.Button(frame, text="✔️ Mark Done", command=mark_done, **btn_style)
mark_btn.grid(row=1, column=1, padx=5, pady=5)

view_btn = tk.Button(frame, text="👀 View Tasks", command=view_tasks, **btn_style)
view_btn.grid(row=2, column=0, padx=5, pady=5)

summary_btn = tk.Button(frame, text="📊 Summary", command=show_summary, **btn_style)
summary_btn.grid(row=2, column=1, padx=5, pady=5)

# Listbox (Task Display)
listbox = tk.Listbox(app, width=50, height=15, font=("Arial", 12), selectbackground="#90ee90")
listbox.pack(pady=15)

# ------------------ Run App ------------------
app.mainloop()
