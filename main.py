import tkinter as tk
import string
import random

def generate_password():
    password_len = int(length_entry.get())
    word = word_entry.get()
    if easy_to_remember.get() == 1:
        password = word + ''.join(random.choices(string.digits, k=password_len-len(word)))
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_len))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def toggle_visibility():
    if password_entry["show"] == "":
        password_entry["show"] = "*"
    else:
        password_entry["show"] = ""

root = tk.Tk()
root.title("Password Generator")

easy_to_remember = tk.IntVar()

word_label = tk.Label(root, text="Word:")
word_label.grid(row=0, column=0, padx=10, pady=10)

word_entry = tk.Entry(root)
word_entry.grid(row=0, column=1, padx=10, pady=10)

length_label = tk.Label(root, text="Length:")
length_label.grid(row=1, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=10)

easy_to_remember_checkbox = tk.Checkbutton(root, text="Easy to remember", variable=easy_to_remember)
easy_to_remember_checkbox.grid(row=4, column=0, columnspan=2, pady=10)

visibility_button = tk.Button(root, text="Show/Hide", command=toggle_visibility)
visibility_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
