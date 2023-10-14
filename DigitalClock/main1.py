import tkinter as tk
from tkinter import font as tkFont
import time
root = tk.Tk()
root.title("Digital Clock")
def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
time_label = tk.Label(root, font=('Helvetica', 48), background='black', foreground='red')
time_label.pack()
update_time()
root.mainloop()