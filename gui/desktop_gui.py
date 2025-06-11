import tkinter as tk
from tkinter import messagebox
from core import calculate_real_size
from db.database import save_specimen, init_db

def submit():
    try:
        username = entry_user.get()
        size = float(entry_size.get())
        magnification = float(entry_mag.get())
        real_size = calculate_real_size(size, magnification)
        save_specimen(username, size, magnification, real_size)
        messagebox.showinfo("Result", f"Real size: {real_size:.2f} units")
    except Exception as e:
        messagebox.showerror("Error", str(e))

init_db()
root = tk.Tk()
root.title("Microscope Size Calculator")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Microscope Size").pack()
entry_size = tk.Entry(root)
entry_size.pack()

tk.Label(root, text="Magnification").pack()
entry_mag = tk.Entry(root)
entry_mag.pack()

tk.Button(root, text="Calculate", command=submit).pack()
root.mainloop()
