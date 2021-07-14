import tkinter


class RowFrame(tkinter.Frame):
    def __init__(self, cols, master, **kwargs):
        super().__init__(master, kwargs)

        self.cols = cols
        self.employer = None

    def draw_button(self, btn_data):
        action_btn = tkinter.Button(self, **btn_data)
        action_btn.pack(side=tkinter.LEFT)

    def draw_entry(self, entry_data):
        self.employer = tkinter.Entry(self, **entry_data)
        self.employer.pack(side=tkinter.LEFT)

    def draw(self):
        for col in self.cols:
            if "justify" in col:
                if "command" in col:
                    self.draw_button(col)
                else:
                    self.draw_entry(col)
            else:
                col_label = tkinter.Label(self, **col)
                col_label.pack(side=tkinter.LEFT)
