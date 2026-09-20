from PresentationLaye.window import Window
from PresentationLaye.Frames.Login import LoginFrame
from PresentationLaye.Frames.Register import RegisterFrame
from tkinter import Frame

class MainView:
    def __init__(self):

        self.frames = {}

        self.window = Window('core bankink')

        self.add_frame('Login',LoginFrame(),400,200)
        self.add_frame('Register',RegisterFrame(),400,200)

        self.show_frame('Login')
        self.window.show()

    def add_frame(self,frame_name:str,frame:Frame,width,height):
        self.frames[frame_name]=(frame,width,height)
        self.frames[frame_name][0].grid(row=0,column=0,sticky='ewsn')

    def show_frame(self,frame_name:str):
        current_frame = self.frames[frame_name]
        current_frame[0].tkraise()

        width , height = self.frames[frame_name][1],self.frames[frame_name][2]

        self.window.resize(width,height)

