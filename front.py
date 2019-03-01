import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import back

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):

        #Studenci
        self.studentList = tk.StringVar()        
        self.studentList.set(back.get_all_students())

        self.studentLabel = tk.Label(self, text="Studenci")        
        self.studentLabel.grid(row=0, column=0)

        self.studentBox = tk.Listbox(self, listvariable=self.studentList)
        self.studentBox.grid(row=1, column=0)        

        #Klasy
        self.classroomList = tk.StringVar()
        self.classroomList.set(back.get_all_classrooms())

        self.classroomLabel = tk.Label(self, text="Klasy")
        self.classroomLabel.grid(row=0, column=1)

        self.classroomBox = tk.Listbox(self, listvariable=self.classroomList)
        self.classroomBox.grid(row=1, column=1)

        #Studenci i ich klasy
        self.studentsAndClassroomsList = tk.StringVar()
        self.studentsAndClassroomsList.set(back.get_students_and_their_classrooms())

        self.studentsAndClassroomsLabel = tk.Label(self, text="Studenci i ich klasy")
        self.studentsAndClassroomsLabel.grid(row=2, column=0, columnspan=2)
        
        self.studentsAndClassroomsBox = tk.Listbox(self, listvariable=self.studentsAndClassroomsList)
        self.studentsAndClassroomsBox.grid(row=3, column=0, columnspan=2)

        # Combobox z nazwami klas
        self.availableClassrooms = ttk.Combobox(self, values=back.get_classroom_names())
        self.availableClassrooms.current(0)
        self.availableClassrooms.grid(row=5, column=0, columnspan=2)

        #Przycisk wyjścia
        self.quitButton = tk.Button(self, text = "Quit", command = lambda: self.display_quit_prompt())
        self.quitButton.grid(row=4, column=0, columnspan=2)
    
    def display_quit_prompt(self):
        result = messagebox.askokcancel(title="Quit application", message="Are you sure to quit application?",
         default=messagebox.OK)

        if not result:
            return

        back.close_cur_and_conn()
        self.quit()

app = Application()
app.master.title('Sample Application')
app.mainloop()