import tkinter as tk

class SchoolDatabaseGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("School Database")

        # Create frames
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)

        # Create widgets for frame 1 (admin)
        self.label1 = tk.Label(self.frame1, text="Student Details")
        self.label1.pack()

        # Create widgets for frame 2 (teacher)
        self.label2 = tk.Label(self.frame2, text="Enter Student ID:")
        self.entry = tk.Entry(self.frame2)
        self.button = tk.Button(self.frame2, text="View Marks", command=self.view_marks)
        self.label2.pack()
        self.entry.pack()
        self.button.pack()

        # Pack frames
        self.frame1.pack(side="left", padx=20)
        self.frame2.pack(side="right", padx=20)

    def view_marks(self):
        # Implement view marks functionality here
        student_id = self.entry.get()
        # Use student_id to retrieve marks from database and display them in a new window or label


root = tk.Tk()
app = SchoolDatabaseGUI(root)
root.mainloop()
