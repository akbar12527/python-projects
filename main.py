import tkinter as tk
import mysql.connector
import datetime
import pytz

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mirzaash22",
    database="testing"
)

root = tk.Tk()
root.geometry('1000x600')


class frame:
    def __init__(self, root):
        # *diplay_frame (Displays todos)
        self.display_frame = tk.Frame(
            root, width=500, height=600, bg='#db9833')
        self.display_frame.place(relx=0.4, rely=0, width=600, height=600)
        # *entry_fram ()
        self.entry_frame = tk.Frame(root, width=400, height=600, bg='#bae2f9')
        self.entry_frame.place(relx=0, rely=0, width=400, height=600)

    def textbox(self):
        self.text_input = tk.Text(self.entry_frame, width=50, height=5)
        self.text_input.place(relx=0, rely=0)
        self.count = -1  # ? counter to keep tracks inputs
        self.task_list = []  # * Task entered action on add_btn ~ todo_list
        # * Tasked packed on display frame ~ display_frame(task displaying frame)
        self.list = []

    def buttons(self):
        # *add button (add todos to display_frame)
        self.add_button = tk.Button(
            self.entry_frame, text='ADD', command=self.todo_list, padx=10, pady=10)
        self.add_button.place(relx=0.86, rely=0.15)
        # *clear button (clear todos from display_frame)
        self.clearlist_button = tk.Button(
            self.entry_frame, text='Clear list', padx=10, pady=10, command=lambda: self.clearlist(self.display_frame))
        self.clearlist_button.place(relx=0.70, rely=0.15)
        # *shows button (data in the database)
        self.show_db = tk.Button(
            self.entry_frame, text='Done Task', padx=20, pady=10, command=self.show_task)
        self.show_db.place(relx=0, rely=0.15)
        # *delete button (deletes all the data from database)
        self.delete_db_data = tk.Button(
            self.entry_frame, text='Delete Data', padx=20, pady=10, command=self.deletedata)
        self.delete_db_data.place(relx=0, rely=0.25)

    def time_details(self):
        self.dt_now = datetime.datetime.now(tz=pytz.UTC)
        self.tmezone = self.dt_now.astimezone(pytz.timezone('Asia/Kolkata'))
        self.current_time = self.tmezone.strftime("%H:%M:%S")

    def push_db(self, text):  # ! push end_time after action on checkbox~todo_list
        self.time_details()
        self.sqlformula_endtime = "UPDATE todolist SET End_time=%s WHERE NAME=%s"
        self.End_time = (self.current_time, text)
        self.mydb_cursor = mydb.cursor()
        self.mydb_cursor.execute(self.sqlformula_endtime, self.End_time)
        mydb.commit()

    def todo_list(self):
        self.count += 1
        self.status = tk.IntVar()
        self.status.set('0')
        self.task = self.text_input.get('1.0', 'end-1c')
        self.task_list.append(self.task)  # * Task every time action on add_btn
        for task in self.task_list:
            if task != '':  # * checker to prevent empty entry
                if task not in self.list:  # * prevent from packing same task repeateadly
                    self.checkbox = tk.Checkbutton(
                        self.display_frame, text=task,
                        variable=self.status, bg='#db9833', pady=3,
                        command=lambda task=task: self.push_db(task))
                    self.checkbox.pack(anchor=tk.W)
                    self.list.append(task)  # * task packed on display_frame
        # ? call database functions and insert value(data,start_time,todoname)
        self.database(self.task)

    def database(self, task):
        self.sqlformula = "INSERT INTO todolist(Date,Start_time,Name) VALUES(%s,%s,%s);"
        self.time_details()
        self.current = (self.tmezone, self.current_time, task)
        self.mydb_cursor = mydb.cursor()
        self.mydb_cursor.execute(self.sqlformula, self.current)
        mydb.commit()

    def show_task(self):
        self.show_window = tk.Toplevel()
        self.show_window.title('Tasks')
        self.show_window.geometry('500x500')
        self.deletequeries = "Delete from todolist where Name=''"
        self.sqlquery_display = "select Date,Start_time,Name,End_time from todolist where Name!=''"
        self.database(task=None)  # ? Calling database to access data
        self.mydb_cursor.execute(self.deletequeries)
        self.mydb_cursor.execute(self.sqlquery_display)
        self.mydb_items = [i for i in self.mydb_cursor]
        # * Lables for database
        self.date_lb = tk.Label(
            self.show_window, text='Date', padx=30, pady=10)
        self.startt_lb = tk.Label(
            self.show_window, text='Start', padx=30, pady=10)
        self.task_lb = tk.Label(
            self.show_window, text='Task', padx=30, pady=10)
        self.endt_lb = tk.Label(self.show_window, text='End', padx=30, pady=10)
        self.date_lb.grid(row=0, column=0)
        self.startt_lb.grid(row=0, column=1)
        self.task_lb.grid(row=0, column=2)
        self.endt_lb.grid(row=0, column=3)
        # ? packing items in database on show_window ~ Toplevel(new window)
        for i in range(4):
            for j in range(1, len(self.mydb_items)):
                self.label = tk.Label(
                    self.show_window, text=self.mydb_items[j][i], padx=30, pady=10)
                self.label.grid(row=j, column=i)
        self.show_window.mainloop()

    def clearlist(self, x):  # * deleting all the widget in display frame ~ display_frame(task window)
        children = x.winfo_children()
        for child in children:
            child.destroy()

    def deletedata(self):  # * clear the data from database
        self.mydb_cursor = mydb.cursor()
        self.mydb_cursor.execute("DELETE FROM todolist")


# ! execution and calling
frm = frame(root)
f = frame.textbox(frm)
btn = frame.buttons(frm)


root.mainloop()
