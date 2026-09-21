from PresentationLaye.component.passworkEntry import PasswordEntry
from tkinter import Frame, Label, Entry, Button, Checkbutton, messagebox
from BusinessLayer.user_busines_logic import UserBusinesLogic


class LoginFrame(Frame):
    def __init__(self,main_window,Main_view,user_business: UserBusinesLogic):
        super().__init__(main_window)

        self.Main_view = Main_view
        self.user_business = user_business

        self.columnconfigure(1, weight=1)

        self.Username_label = Label(self, text='Username')
        self.Username_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.Username_entry = Entry(self)
        self.Username_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky='ew')

        self.Password_label = Label(self, text='Password')
        self.Password_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='e')

        self.Password_entry = PasswordEntry(self)
        self.Password_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky='ew')

        self.Chek_button = Checkbutton(self, text='Remember me')
        self.Chek_button.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky='w')

        self.Login_buttom = Button(self, text='Login', command=self.login_button_clicked)
        self.Login_buttom.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky='we')

        self.Register_buttom = Button(self, text='Register',command=self.register_button_clicked)
        self.Register_buttom.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky='we')

    def login_button_clicked(self):
        username = self.Username_entry.get()
        password = self.Password_entry.get_value()

        response = self.UserBusinesLogic.Login(username, password)

        if response.succes:
            messagebox.showinfo(message='Login Successful')
        else:
            messagebox.showerror("Login Failed", response.message)

    def register_button_clicked(self):
        self.Main_view.show_frame('Register')
