# from tkinter import Tk, mainloop
from ttkbootstrap import Window

# class Window(Tk):
#     def __init__(self,title="User Management Application"):
#         super().__init__()
#         self.title(title)
#         self.geometry("400x300")
#
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0,weight=1)
#
#     def show(self):
#         self.mainloop()


class MainWindow(Window):
    def __init__(self,title="User Management Application",iconphoto="images/user_management_profile.png"):
        super().__init__()
        self.title(title)
        # self.iconphoto(iconphoto)
        self.geometry("400x300")


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)

    def show(self):
        self.mainloop()