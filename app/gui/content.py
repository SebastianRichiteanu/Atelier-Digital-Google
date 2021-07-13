import tkinter
from .employees import EmployeesFrame


class ContentFrame(tkinter.Frame):
    def __init__(self, fire, hire, master, **kwargs):
        super().__init__(master, kwargs)

        self.master = master
        self.brand_label = None
        self.employees_frame = None
        self.fire = fire
        self.hire = hire
        self.current_employer = tkinter.StringVar("")

    def draw(self, brand_name="N/A", users=None):
        if not users:
            users = []

        self.brand_label = tkinter.Label(
            master=self,
            text=brand_name,
            bg="#fff",
            fg="#000",
            font=("Arial", 24, "bold"),
        )
        self.brand_label.pack(side=tkinter.TOP)

        self.current_employer.set(brand_name)

        self.employees_frame = EmployeesFrame(users, self.fire, self.hire, self.current_employer, self, bg="#fff", pady=10)
        self.employees_frame.pack(side=tkinter.TOP)
        self.employees_frame.draw()

    def change_employer_name(self, employer):
        self.brand_label['text'] = employer.name
        self.current_employer.set(employer.name)
        self.employees_frame.draw()


