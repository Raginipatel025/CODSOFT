import tkinter as tk
from tkinter import messagebox
import random

# ---------------- Game Logic ----------------
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    # Determine result
    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You Win!"
        user_score += 1
    else:
        result = "💻 Computer Wins!"
        computer_score += 1

    # Update UI
    user_choice_label.config(text=f"🧑 You chose: {user_choice}")
    computer_choice_label.config(text=f"💻 Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="🧑 You chose: ")
    computer_choice_label.config(text="💻 Computer chose: ")
    result_label.config(text="Result will appear here")
    score_label.config(text="Score → You: 0 | Computer: 0")

# ---------------- GUI Setup ----------------
app = tk.Tk()
app.title("✊✋✌ Rock-Paper-Scissors Game")
app.geometry("500x450")
app.config(bg="#121212")

# Title
title = tk.Label(app, text="Rock-Paper-Scissors", font=("Helvetica", 20, "bold"), bg="#121212", fg="#00e5ff")
title.pack(pady=15)

# Instructions
instructions = tk.Label(app, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 12), bg="#121212", fg="white")
instructions.pack(pady=5)

# Buttons
button_frame = tk.Frame(app, bg="#121212")
button_frame.pack(pady=10)

btn_style = {"width": 12, "height": 2, "font": ("Helvetica", 12, "bold")}

rock_btn = tk.Button(button_frame, text="✊ Rock", command=lambda: play("Rock"), bg="#ff5252", fg="white", **btn_style)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="✋ Paper", command=lambda: play("Paper"), bg="#4caf50", fg="white", **btn_style)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✌ Scissors", command=lambda: play("Scissors"), bg="#2979ff", fg="white", **btn_style)
scissors_btn.grid(row=0, column=2, padx=10)

# Display Results
user_choice_label = tk.Label(app, text="🧑 You chose: ", font=("Helvetica", 12), bg="#121212", fg="white")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(app, text="💻 Computer chose: ", font=("Helvetica", 12), bg="#121212", fg="white")
computer_choice_label.pack(pady=5)

result_label = tk.Label(app, text="Result will appear here", font=("Helvetica", 14, "bold"), bg="#121212", fg="#ffeb3b")
result_label.pack(pady=10)

score_label = tk.Label(app, text="Score → You: 0 | Computer: 0", font=("Helvetica", 12, "bold"), bg="#121212", fg="#00e676")
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(app, text="🔄 Reset Game", command=reset_game, bg="#ff9800", fg="white", font=("Helvetica", 12, "bold"), width=20)
reset_btn.pack(pady=15)

# Run App
app.mainloop()
