from tkinter import Entry, Button, Label, Checkbutton, Frame
from PresentationLaye.component.passworkEntry import PasswordEntry


class RegisterFrame(Frame):
    def __init__(self, ):
        super().__init__()

        self.user_name_label = Label(self, text='Username')
        self.user_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.user_name_entry = Entry(self)
        self.user_name_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky='ew')

        self.password_label = Label(self, text='Password')
        self.password_label.grid(row=1, column=0, padx=10, pady=(0,10), sticky='e')

        self.password_entry = PasswordEntry(self)
        self.password_entry.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky='ew')