import tkinter
from .employees import EmployeesFrame
from .employers import EmployersFrame


class ContentFrame(tkinter.Frame):
    def __init__(self, fire, hire, add_employer, delete_employer, edit_employer, master, **kwargs):
        super().__init__(master, kwargs)

        self.master = master
        self.brand_label = None
        self.employees_frame = None
        self.fire = fire
        self.hire = hire
        self.current_employer = tkinter.StringVar("")

        self.add_employer = add_employer
        self.delete_employer = delete_employer
        self.edit_employer = edit_employer
        self.employers_frame = None

    def draw(self, brand_name="N/A", users=None, employers=None, window="main"):
        if window == "main":
            self.draw_main(brand_name, users)
        else:
            self.draw_employers(employers)

    def draw_main(self, brand_name, users):
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

    def draw_employers(self, employers):
        if not employers:
            employers = []

        self.employers_frame = EmployersFrame(employers, self.add_employer, self.delete_employer, self.edit_employer,
                                              self, bg="#fff", pady=10)
        self.employers_frame.pack(side=tkinter.TOP)
        self.employers_frame.draw()

    def change_employer_name(self, employer):
        self.brand_label['text'] = employer.name
        self.current_employer.set(employer.name)
        self.employees_frame.draw()


