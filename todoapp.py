import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.listbox = tk.Listbox(self.frame, height=15, width=50)
        self.listbox.pack(side=tk.LEFT)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(self.root, text="Complete Task", width=48, command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append({'task': task, 'completed': False})
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]['completed'] = True
            self.listbox.delete(index)
            self.listbox.insert(index, self.tasks[index]['task'] + " (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks.pop(index)
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "You shouldselect a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
