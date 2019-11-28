import tkinter as tk
import os
import time

root = tk.Tk()


button = tk.Button(root, text='click me')
button.pack()
label = tk.Label(root, text='heloo world')
label.pack()
root.maintloop()
