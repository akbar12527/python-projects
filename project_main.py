import tkinter as tk
import os
import time

root = tk.Tk()
root.title('T0D0')


class canvas:
    def __init__(self, root):

        self.input_canvas = tk.Canvas(
            root, width=300, height=600, bg='#e9ab18')
        self.input_canvas.grid(row=0, column=0)

        self.diplay_canvas = tk.Canvas(
            root, width=500, height=600, bg='#f5d997')
        self.diplay_canvas.grid(row=0, column=1)


class buttons:
    def __init__(self, canvas):
        self.add_button = tk.Button(canvas, text='ADD')
        self.add_button.place(relx=0, rely=0)


can = canvas(root)

buttons(can.input_canvas)


root.mainloop()
