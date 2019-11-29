import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

txt = tk.Text(root, height=5, width=50)
txt.pack()
btn = tk.Button(root, text='click me',
                command=lambda: display(txt.get('1.0', 'end-1c')))
btn.pack()
frame = tk.Frame(root, bg='#f5d997')
frame.grid(row=1, column=0)


def display(text):
    checkbtn = tk.Checkbutton(frame, text=text, bg='#f5d997')
    checkbtn.pack()


root.mainloop()
