from ttkbootstrap import Frame ,Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic

class LoginFrame(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)

        self.main_view=main_view
        self.grid_columnconfigure(1,weight=1)

        self.user_business_logic=UserBusinessLogic()

        self.title_lable=Label(self,text="Login Frame")
        self.title_lable.grid(row=0,column=1,pady=10)

        self.username_lable=Label(self,text="Username")
        self.username_lable.grid(row=1,column=0,padx=5,pady=(0,5),sticky="e")

        self.username_entry=Entry(self)
        self.username_entry.grid(row=1,column=1,padx=(5,10),pady=(0,5),sticky="ew")

        self.password_lable = Label(self, text="Password")
        self.password_lable.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="e")

        self.password_entry = Entry(self,show="*")
        self.password_entry.grid(row=2, column=1, padx=(5, 10), pady=(0, 5),sticky="ew")

        self.show_password_button=Button(self,text="@@",)
        self.show_password_button.grid(row=2, column=1, padx=(5, 10),sticky="e")

        self.login_button=Button(self,text="Login",command=self.login)
        self.login_button.grid(row=3, column=1, padx=(5, 10), pady=(0, 5),sticky="w")

        self.register_button = Button(self, text="Register",command=self.register)
        self.register_button.grid(row=4, column=1, padx=(5, 10), pady=(0, 5),sticky="w")

    def login(self):
        username=self.username_entry.get()
        password=self.password_entry.get()

        result=self.user_business_logic.login(username,password)
        if result.success:
            # messagebox.showinfo("Information",f"welcome {result.data.get_fullname()}")
            home_frame=self.main_view.switch_frame("home")
            home_frame.set_current_user(result.data)

            self.username_entry.delete(0,"end")
            self.password_entry.delete(0,"end")

        else:
            Messagebox.show_info(f"{result.mesage}","Error")

    def register(self):
        self.main_view.switch_frame("register")