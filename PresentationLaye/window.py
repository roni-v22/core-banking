from tkinter import Tk,Button


class Window(Tk):
    def __init__(self,title_name):
        super().__init__()

        self.title = title_name

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.back_button=Button(self,text='go back')
        self.back_button.grid(row=0,column=0,padx=10,pady=10)


    def resize(self,width,height):
        self.geometry(f'{width}x{height}')

    def show(self):
        self.mainloop()
