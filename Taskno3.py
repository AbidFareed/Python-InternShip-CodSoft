import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    scope = string.ascii_letters
    if complexity == "Medium":
        scope += string.digits
    elif complexity == "High":
        scope += string.digits + string.punctuation
    password = ''.join(random.choice(scope) for _ in range(length))
    return password

def generate_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive number.")
            return

        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        password_label.config(text=f"Generated Password:\n{password}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

interface = tk.Tk()
interface.title("Password Generator")

length_label = tk.Label(interface, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(interface)
length_entry.pack()

complexity_label = tk.Label(interface, text="Password Complexity:")
complexity_label.pack(pady=5)

complexity_var = tk.StringVar()
complexity_var.set("Low")
complexity_menu = tk.OptionMenu(interface, complexity_var, "Low", "Medium", "High")
complexity_menu.pack(pady=5)

generate_button = tk.Button(interface, text="Generate Password", command=generate_button_click)
generate_button.pack(pady=5)

password_label = tk.Label(interface, text="")
password_label.pack()

interface.mainloop()
