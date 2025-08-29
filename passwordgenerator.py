import tkinter as tk
from tkinter import messagebox
import random, string

# ---------------- Password Generator Function ----------------
def generate_password():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        if length < 4:
            messagebox.showwarning("⚠️ Warning", "Password length must be at least 4!")
            return

        if complexity == "Easy":
            characters = string.ascii_letters
        elif complexity == "Strong":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + string.punctuation

        global generated_password
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"🔑 Password: {generated_password}")
    
    except ValueError:
        messagebox.showerror("❌ Error", "Please enter a valid number for length.")

# ---------------- Copy to Clipboard ----------------
def copy_to_clipboard():
    if generated_password:
        app.clipboard_clear()
        app.clipboard_append(generated_password)
        messagebox.showinfo("✅ Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("⚠️ Warning", "No password generated yet!")

# ---------------- Theme Toggle ----------------
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        app.config(bg="#121212")
        title.config(bg="#121212", fg="#00e5ff")
        length_label.config(bg="#121212", fg="white")
        complexity_label.config(bg="#121212", fg="white")
        result_label.config(bg="#121212", fg="#ffeb3b")
        for rb in radio_buttons:
            rb.config(bg="#121212", fg="white", selectcolor="#1e1e1e", activebackground="#121212")
    else:
        app.config(bg="#f0f0f0")
        title.config(bg="#f0f0f0", fg="#222")
        length_label.config(bg="#f0f0f0", fg="#000")
        complexity_label.config(bg="#f0f0f0", fg="#000")
        result_label.config(bg="#f0f0f0", fg="blue")
        for rb in radio_buttons:
            rb.config(bg="#f0f0f0", fg="black", selectcolor="#f0f0f0", activebackground="#f0f0f0")

# ---------------- GUI Setup ----------------
app = tk.Tk()
app.title("🔒 Password Generator")
app.geometry("460x420")

generated_password = ""
dark_mode = True  # Default: Dark Mode

# Title
title = tk.Label(app, text="🔐 Password Generator", font=("Helvetica", 20, "bold"))
title.pack(pady=15)

# Password Length Input
length_label = tk.Label(app, text="Enter Password Length:", font=("Helvetica", 12))
length_label.pack()
length_entry = tk.Entry(app, width=10, font=("Helvetica", 14))
length_entry.pack(pady=8)

# Complexity Options
complexity_label = tk.Label(app, text="Select Complexity:", font=("Helvetica", 12))
complexity_label.pack(pady=5)
complexity_var = tk.StringVar(value="Strong")

radio_buttons = []
style = {"font": ("Helvetica", 11)}
rb1 = tk.Radiobutton(app, text="Easy (Only Letters)", variable=complexity_var, value="Easy", **style); rb1.pack()
rb2 = tk.Radiobutton(app, text="Strong (Letters + Numbers)", variable=complexity_var, value="Strong", **style); rb2.pack()
rb3 = tk.Radiobutton(app, text="Very Strong (Letters + Numbers + Symbols)", variable=complexity_var, value="Very Strong", **style); rb3.pack()
radio_buttons.extend([rb1, rb2, rb3])

# Generate Button
generate_btn = tk.Button(app, text="⚡ Generate Password", command=generate_password,
                         bg="#00c853", fg="white", font=("Helvetica", 13, "bold"), width=22, height=2)
generate_btn.pack(pady=10)

# Result Label
result_label = tk.Label(app, text="🔑 Password: ", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

# Copy Button
copy_btn = tk.Button(app, text="📋 Copy to Clipboard", command=copy_to_clipboard,
                     bg="#2979ff", fg="white", font=("Helvetica", 13, "bold"), width=22, height=2)
copy_btn.pack(pady=8)

# Theme Toggle Button
theme_btn = tk.Button(app, text="🌙 Toggle Dark/Light Mode", command=toggle_theme,
                      bg="#ff9800", fg="white", font=("Helvetica", 12, "bold"))
theme_btn.pack(pady=15)

# Apply initial theme
apply_theme()

# Run App
app.mainloop()
