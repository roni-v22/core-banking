from tkinter import Entry, Button, Label, Checkbutton, Frame
from PresentationLaye.component.passworkEntry import PasswordEntry


class RegisterFrame(Frame):
    def __init__(self,main_window,Main_view):
        super().__init__(main_window)

        self.Main_view = Main_view

        self.grid_columnconfigure(1, weight=1)

        self.user_name_label = Label(self, text='Username')
        self.user_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.user_name_entry = Entry(self)
        self.user_name_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky='ew')

        self.password_label = Label(self, text='Password')
        self.password_label.grid(row=1, column=0, padx=10, pady=(0,10), sticky='e')

        self.password_entry = PasswordEntry(self)
        self.password_entry.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky='ew')

        self.firstname_label = Label(self, text='First Name')
        self.firstname_label.grid(row=2, column=0, padx=10, pady=(0,10), sticky='e')

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=2, column=1, padx=(0, 10), pady=(0,10), sticky='ew')

        self.lastname_label = Label(self, text='Last Name')
        self.lastname_label.grid(row=3, column=0, padx=10, pady=(0,10), sticky='e')

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=3, column=1, padx=(0, 10), pady=(0,10), sticky='ew')

        self.remember_me_checkbutton = Checkbutton(self, text='remember me')
        self.remember_me_checkbutton.grid(row=4, column=1, padx=10, pady=(0,10), sticky='w')

        self.regester_button = Button(self, text='Register')
        self.regester_button.grid(row=5, column=1, padx=10, pady=(0,10), sticky='ew')

        self.back_to_login_button = Button(self, text='Back',command=self.back_to_login_button_clicked)
        self.back_to_login_button.grid(row=6, column=1, padx=10, pady=(0,10), sticky='ew')

    def back_to_login_button_clicked(self):
        self.Main_view.show_frame('Login')
