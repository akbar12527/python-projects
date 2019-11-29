import tkinter as tk
import os
import time
import mysql

root = tk.Tk()
root.title('T0D0')


class canvas:
    def __init__(self, root):

        self.input_canvas = tk.Canvas(
            root, width=300, height=600, bg='#e9ab18')
        self.input_canvas.grid(row=0, column=0)

        self.diplay_canvas = tk.Canvas(
            root, width=500, height=600, bg='#f5d997')
        # self.diplay_canvas.grid(row=0, column=1)
class frame:
    def __init__(self,root):
        self.display_frame=tk.Frame(root,height=600,width=500,bg='#f5d997')
        self.display_frame.grid(row=0,column=1)

class buttons:
    def __init__(self, frame):
        self.add_button = tk.Button(frame, text='ADD')
        self.add_button.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.1)

        self.clear_button = tk.Button(frame, text='CLEAR')
        self.clear_button.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.1)

class inputs:
    def __init__(self, canvas):
        self.input_box = tk.Text(canvas, height=1, width=50)
        self.input_box.place(relx=0.1, rely=0.070, relwidth=0.8,
                            relheight=0.1)

        # self.input_text=input_box.get()

class todo_list:
    def __init__(self,display_frame,input_text):
        pass
    def checkboxes(self,display_frame,input_text):
        self.checkbox=tk.Checkbutton(display_frame,text=input_text)
        self.checkbox.grid(row=0,column=0)

# CLASS CALLING
can = canvas(root)
frm=frame(root)
buttons(can.input_canvas)

inp=inputs(can.input_canvas)
# td=todo_list.checkboxes(frm,inp.input_text)

root.mainloop()
