import tkinter
from .generic_frames import RowFrame


class EmployerFrame(tkinter.Frame):
    def __init__(self, employer, edit, delete, bg_color, master, **kwargs):
        super().__init__(master, kwargs)

        self.employer = employer
        self.edit = edit
        self.delete = delete
        self.bg_color = bg_color
        self.row_frame = None

    def draw(self):
        if self.row_frame is not None:
            self.row_frame.pack_forget()

        name_field = {
            "text": self.employer.name,
            "bg": self.bg_color,
            "font": ("Arial", 12, "normal"),
            "padx": 10,
            "width": 15 if "@" not in self.employer.name else 30,
        }
        col_props2 = [name_field, self.btn_edit(), self.btn_delete()]

        self.row_frame = RowFrame(col_props2, self, bg=self.bg_color)
        self.row_frame.pack(side=tkinter.TOP)
        self.row_frame.draw()

    def draw_edit(self):
        if self.row_frame is not None:
            self.row_frame.pack_forget()

        col_props2 = [self.entry(), self.btn_submit(), self.btn_cancel()]

        self.row_frame = RowFrame(col_props2, self, bg=self.bg_color)
        self.row_frame.pack(side=tkinter.TOP)
        self.row_frame.draw()

    def btn_delete(self):
        return {
            "fg": "#fff",
            "bg": "#800000",
            "activebackground": "#990000",
            "activeforeground": "#fff",
            "text": "Delete",
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "padx": 10,
            "width": 15,
            "command": self.delete_employer,
        }

    def btn_edit(self):
        return {
            "fg": "#fff",
            "bg": "#008000",
            "activebackground": "#009900",
            "activeforeground": "#fff",
            "text": "Edit",
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "padx": 10,
            "width": 15,
            "command": self.edit_employer,
        }

    def btn_submit(self):
        return {
            "fg": "#fff",
            "bg": "#008000",
            "activebackground": "#009900",
            "activeforeground": "#fff",
            "text": "Submit",
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "padx": 10,
            "width": 15,
            "command": self.submit_edit,
        }

    def btn_cancel(self):
        return {
            "fg": "#fff",
            "bg": "#800000",
            "activebackground": "#990000",
            "activeforeground": "#fff",
            "text": "Cancel",
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "padx": 10,
            "width": 15,
            "command": self.cancel_edit,
        }

    def entry(self):
        return {
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "width": 15,
        }

    def delete_employer(self):
        self.delete(self.employer)
        self.row_frame.pack_forget()


    def edit_employer(self):
        self.row_frame.pack_forget()
        self.draw_edit()
        self.row_frame.employer.insert(0, self.employer.name)

    def submit_edit(self):
        new_name = self.row_frame.employer.get()
        self.employer.name = new_name
        self.edit(self.employer.name, new_name)
        self.row_frame.pack_forget()
        self.draw()

    def cancel_edit(self):
        self.row_frame.pack_forget()
        self.draw()


class NewEmployerFrame(tkinter.Frame):
    def __init__(self, add, bg_color, master, **kwargs):
        super().__init__(master, kwargs)

        self.add = add
        self.bg_color = bg_color
        self.row_frame = None
        self.name = "test"

    def draw(self):
        if self.row_frame is not None:
            self.row_frame.pack_forget()

        col_props = [self.entry(), self.btn_add()]

        self.row_frame = RowFrame(col_props, self, bg=self.bg_color)
        self.row_frame.pack(side=tkinter.TOP)
        self.row_frame.draw()

    def btn_add(self):
        return {
            "fg": "#fff",
            "bg": "#800000",
            "activebackground": "#990000",
            "activeforeground": "#fff",
            "text": "Add",
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "padx": 10,
            "width": 15,
            "command": self.add_employer,
        }

    def entry(self):
        return {
            "font": ("Arial", 12, "normal"),
            "justify": tkinter.CENTER,
            "width": 15,
        }

    def add_employer(self):
        self.add(self.row_frame.employer.get())


class EmployersFrame(tkinter.Frame):
    def __init__(self, employers, add, delete, edit, master, **kwargs):
        super().__init__(master, kwargs)

        self.employers = employers
        self.add = add
        self.delete = delete
        self.employers_rows = []
        self.edit = edit

    def draw_header(self):
        header_cols = list(map(lambda header_value: {
            "text": header_value,
            "bg": "#eee",
            "font": ("Arial", 12, "bold"),
            "padx": 10,
            "width": 15 if header_value != "EMAIL" else 30,
        }, ["NAME", "EDIT", "DELETE"]))

        header_frame = RowFrame(header_cols, self, bg="#eee")
        header_frame.pack(side=tkinter.TOP)
        header_frame.draw()

    def draw(self):
        if len(self.employers_rows):
            for row in self.employers_rows:
                row.pack_forget()
        else:
            self.draw_header()

        for index, employer in enumerate(self.employers):
            row_color = "#fff" if index % 2 == 0 else "#eee"
            employer_frame = EmployerFrame(
                employer,
                self.edit,
                self.delete,
                row_color,
                self,
                bg=row_color,
                padx=10,
                pady=10,
            )
            employer_frame.pack(side=tkinter.TOP)
            employer_frame.draw()
            self.employers_rows.append(employer_frame)

        new_employer_frame = NewEmployerFrame(
            self.add,
            "#fff",
            self,
            bg="#fff",
            padx=10,
            pady=10,
        )
        new_employer_frame.pack(side=tkinter.TOP)
        new_employer_frame.draw()
