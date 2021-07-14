import tkinter
from .content import ContentFrame
from handlers.employees import fire, hire
from handlers.employers import *


class GUI:
    """This class is responsible for drawing the GUI."""
    def __init__(self):
        self.width = 800
        self.height = 700

        self.window = tkinter.Tk()
        self.window.title("GAD 06 Desktop Apps")
        self.window.geometry(f'{self.width}x{self.height}')
        self.window.configure(background="#fff", padx=10, pady=10)
        self.content_frame = None
        self.loading_label = None
        self.is_content_loading = True
        self.employers = []
        self.users = []
        # Dropdown
        self.current_employer = None
        self.dropdown_name = tkinter.StringVar(self.window)
        self.dropdown = None
        # Employers menu
        self.employers_button = tkinter.Button(self.window, text="Employers", command=self.go_to_employers)

    def set_data(self, users=None, employers=None):
        self.is_content_loading = False

        if not users:
            users = []

        if not employers:
            employers = []

        self.employers = employers
        self.users = users

        self.current_employer = employers[0] if len(employers) > 0 else None
        self.dropdown_name.set(self.current_employer.name)

        name_list = [x.name for x in employers]
        self.dropdown = tkinter.OptionMenu(self.window, self.dropdown_name, *name_list, command=self.change_employer)

        self.draw(brand_name=self.current_employer.name, users=users)

    def go_to_employers(self):
        self.content_frame.pack_forget()
        self.dropdown.pack_forget()
        self.employers_button.config(text="Back")
        self.employers_button.config(command=self.go_to_default_menu)
        self.draw(brand_name=self.current_employer.name, users=self.users, employers=self.employers, window="employers")

    def go_to_default_menu(self):
        self.content_frame.pack_forget()
        self.dropdown.pack_forget()
        self.draw(brand_name=self.current_employer.name, users=self.users, employers=self.employers)
        self.employers_button.config(text="Employers")
        self.employers_button.config(command=self.go_to_employers)

    def find_employer_by_name(self, name):
        for employer in self.employers:
            if employer.name == name:
                return employer
        return None

    def change_employer(self, employer_name):
        new_employer = self.find_employer_by_name(employer_name)
        self.current_employer = new_employer
        self.content_frame.change_employer_name(new_employer)

    def refresh_employers(self):
        self.go_to_default_menu()
        self.go_to_employers()

    def fire(self, user):
        fire(user, self.current_employer)

    def hire(self, user):
        hire(user, self.current_employer)

    def add_employer(self, employer_name):
        add_employer(employer_name)
        self.employers.append(Employer(name=employer_name))
        self.refresh_employers()

    def delete_employer(self, employer):
        delete_employer(employer)
        self.employers.remove(employer)
        self.refresh_employers()

    def edit_employer(self, old_employer, new_employer):
        edit_employer(old_employer, new_employer)

    def draw(self, brand_name=None, users=None, employers=None, window="main"):
        if self.is_content_loading:
            self.loading_label = tkinter.Label(
                master=self.window,
                bg="#fff",
                fg="#424242",
                text="Loading ...",
                font=("Arial", 24, "bold")
            )
            self.loading_label.pack(side=tkinter.TOP)
        else:
            self.loading_label.pack_forget()
            self.employers_button.pack(side=tkinter.TOP, anchor=tkinter.NW)
            if window == "main":
                if employers is not None:
                    name_list = [x.name for x in employers]
                    self.dropdown = tkinter.OptionMenu(self.window, self.dropdown_name, *name_list,
                                                       command=self.change_employer)
                self.dropdown.pack()
            self.content_frame = ContentFrame(
                self.fire,
                self.hire,
                self.add_employer,
                self.delete_employer,
                self.edit_employer,
                self.window,
                bg="#fff",
                width=self.width,
                height=self.height,
            )
            self.content_frame.pack(side=tkinter.TOP)
            self.content_frame.pack_propagate(False)
            self.content_frame.draw(brand_name=brand_name, users=users, employers=employers, window=window)

    def show(self):
        self.draw()
        self.window.mainloop()
