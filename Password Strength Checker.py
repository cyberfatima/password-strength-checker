import tkinter as tk
from tkinter import ttk
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[@$!%*?&]', password):
        score += 1

    if score == 5:
        strength = "Strong"
        color = "green"
    elif score >= 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    return strength, score, color


# Live password strength update
def on_password_change(event=None):
    pwd = password_entry.get()
    strength, score, color = check_password_strength(pwd)
    strength_label.config(text=f"Strength: {strength}", fg=color)
    progress['value'] = score
    style.configure("TProgressbar", troughcolor="white", background=color)


# Toggle password visibility
def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="Hide")


# Copy password to clipboard
def copy_to_clipboard():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        root.update()
        copy_label.config(text="Copied!", fg="blue")
        root.after(1500, lambda: copy_label.config(text=""))


# --- GUI Setup ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x350")
root.resizable(False, False)

# Guidelines
guidelines = (
    "Password Guidelines:\n"
    "• At least 8 characters long\n"
    "• Contains uppercase & lowercase letters\n"
    "• Contains numbers\n"
    "• Contains special characters (@, $, !, %, *, ?, &)"
)
tk.Label(root, text=guidelines, justify="left", anchor="w").pack(pady=5)

# Password entry + buttons
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Enter Password:").grid(row=0, column=0, padx=5)
password_entry = tk.Entry(frame, show="*", width=25)
password_entry.grid(row=0, column=1, padx=5)
password_entry.bind("<KeyRelease>", on_password_change)

toggle_btn = tk.Button(frame, text="Show", command=toggle_password)
toggle_btn.grid(row=0, column=2, padx=5)

copy_btn = tk.Button(frame, text="Copy", command=copy_to_clipboard)
copy_btn.grid(row=0, column=3, padx=5)

copy_label = tk.Label(root, text="", font=("Arial", 9))
copy_label.pack()

# Strength label
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
strength_label.pack(pady=5)

# Progress bar
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TProgressbar", thickness=20)

progress = ttk.Progressbar(root, length=250, maximum=5, mode='determinate')
progress.pack(pady=10)

root.mainloop()
