from tkinter import Entry, Button, Frame


class PasswordEntry(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        self.Password_Entry = Entry(self, show='*')
        self.Password_Entry.grid(row=0, column=0, sticky='we')

        self.change_state_button = Button(self, text='show', command=self.change_state)
        self.change_state_button.grid(row=0, column=1, sticky='w')

    def change_state(self):
        current_value = self.change_state_button.cget('text')

        if current_value == 'show':
            self.change_state_button.config(text='Hide')
            self.Password_Entry.config(show='')
        else:
            self.change_state_button.config(text='Show')
            self.Password_Entry.config(show='*')

    def get_value(self):
        value = self.Password_Entry.get()
        return value
