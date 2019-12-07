import tkinter as tk

<<<<<<< HEAD
=======

>>>>>>> master2
root = tk.Tk()
root.geometry('1000x600')


class frame:
    def __init__(self, root):
        self.display_frame = tk.Frame(
            root, width=500, height=600, bg='#db9833')
        self.display_frame.place(relx=0.4, rely=0, width=600, height=600)

        self.entry_frame = tk.Frame(root, width=400, height=600, bg='#bae2f9')
        self.entry_frame.place(relx=0, rely=0, width=400, height=600)

    def textbox(self):
        self.text_input = tk.Text(self.entry_frame, width=50, height=5)
        self.text_input.place(relx=0, rely=0)
        # self.store_text = self.text_input.get('1.0', 'end-1c')

    def buttons(self):
<<<<<<< HEAD
        self.add_button = tk.Button(
            self.entry_frame, text='ADD', command=self.todo_list, padx=10, pady=10)
        self.add_button.place(relx=0.86, rely=0.15)
=======
        # add button
        self.add_button = tk.Button(
            self.entry_frame, text='ADD', command=self.todo_list, padx=10, pady=10)
        self.add_button.place(relx=0.86, rely=0.15)
        # clear button
        self.clearlist_button = tk.Button(
            self.entry_frame, text='Clear list', command=lambda: self.clearlist(self.display_frame), padx=10, pady=10)
        self.clearlist_button.place(relx=0.69, rely=0.15)
>>>>>>> master2

    def todo_list(self):
        self.checkbox = tk.Checkbutton(
            self.display_frame, text=self.text_input.get('1.0', 'end-1c'), bg='#db9833', pady=3)
        self.checkbox.pack(anchor=tk.W)

<<<<<<< HEAD
=======
    def clearlist(self, x):
        children = x.winfo_children()
        for child in children:
            child.destroy()

>>>>>>> master2

frm = frame(root)
f = frame.textbox(frm)
btn = frame.buttons(frm)

root.mainloop()
