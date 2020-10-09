import tkinter as tk
from tkinter import ttk
import data_layer


class Window(tk.Tk):
    def __init__(self, task_data):
        super().__init__()
        self.resizable(False, False)
        self.title("To-Do List")
        self.task_list = [0]    # keeps track of how many tasks are on screen
        self.entry_dict = {}    # keeps track of the checkboxes and their related entries on screen

        # build the initial window
        self.top_frame = tk.Frame(width=40)
        self.bottom_frame = tk.Frame()
        self.title_label = tk.Label(master=self.top_frame, text="To-Do")
        self.add_task_button = tk.Button(master=self.top_frame, text="Add Task", command=self.add_task)
        self.delete_task_button = tk.Button(master=self.top_frame, text="Delete Task", command=self.delete_task)
        self.save_button = tk.Button(master=self.top_frame, text="Save", command=lambda: self.save_tasks(task_data))

        self.add_task_button.pack(side=tk.RIGHT)
        self.delete_task_button.pack(side=tk.RIGHT)
        self.save_button.pack(side=tk.RIGHT)
        self.title_label.pack(side=tk.LEFT)
        self.top_frame.pack(fill=tk.X, expand=True)
        self.bottom_frame.pack()

        # add tasks read from database to screen
        task_data.read_tasks()
        for value in task_data.task_list:
            self.add_task(value)

    # saves the tasks on screen to a csv file
    def save_tasks(self, tasks_data):
        tasks_data.task_list = []
        for value in self.entry_dict.values():
            tasks_data.task_list.append(value.get())
        tasks_data.write_tasks()

    # adds a new checkbox and entry to the screen
    def add_task(self, task_str=""):
        self.task_list.append(int(self.task_list[-1])+1)

        # create new checkbox and entry widgets with given text
        new_checkbox = ttk.Checkbutton(self.bottom_frame)
        new_checkbox.state(['!alternate'])
        new_entry = tk.Entry(self.bottom_frame, width=40)
        new_entry.insert(0, task_str)

        # add new widgets to dictionary
        self.entry_dict[new_checkbox] = new_entry

        new_checkbox.grid(row=int(self.task_list[-1]), column=1)
        new_entry.grid(row=int(self.task_list[-1]), column=2)

    # deletes selected tasks from screen
    def delete_task(self):
        tmp_lst = []    # keeps track of all checkboxes that are removed
        tmp = 0     # counts how many lines are removed

        # checks which boxes are checked and removes them and their related entry from the screen
        for key, value in self.entry_dict.items():
            if key.instate(['selected']):
                key.destroy()
                value.destroy()
                tmp_lst.append(key)
                tmp += 1

        # removes deleted widgets from dictionary
        for i in tmp_lst:
            del self.entry_dict[i]

        # sets task_list to the new amount of lines on the screen
        for i in range(tmp):
            self.task_list.pop()


task_database = data_layer.TaskDatabase()

window = Window(task_database)

window.mainloop()
