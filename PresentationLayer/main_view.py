from PresentationLayer.Frames.home import HomeFrame
from PresentationLayer.Frames.register import RegisterFrame
from PresentationLayer.Frames.user_management import UserManagement
from PresentationLayer.window import Window
from PresentationLayer.Frames.login import LoginFrame


class MainView:
    def __init__(self):
        self.window = Window()
        self.frames = {}

        self.add_frame("user_management", UserManagement(self.window, self))
        self.add_frame("register",RegisterFrame(self.window,self))
        self.add_frame("home", HomeFrame(self.window,self))
        self.add_frame("login",LoginFrame(self.window,self))

        self.window.show()


    def add_frame(self, name, frame):
        self.frames[name] = frame
        frame.grid(row=0,column=0,sticky="nsew")

    def switch_frame(self,name):
        frame=self.frames[name]
        frame.tkraise()
        return frame