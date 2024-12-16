from ttkbootstrap import Frame,Button,Label,Entry
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic

class RegisterFrame(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)

        self.main_view=main_view

        self.grid_columnconfigure(1,weight=1)

        self.user_business_logic=UserBusinessLogic()

        self.first_name_label=Label(self,text="Firstname")
        self.first_name_label.grid(row=0,column=0,padx=5,pady=(10,5),sticky="e")

        self.first_name_entry=Entry(self)
        self.first_name_entry.grid(row=0,column=1,padx=(0,10),pady=(10,5),sticky="ew")

        self.last_name_label=Label(self,text="Lastname")
        self.last_name_label.grid(row=1,column=0,padx=5,pady=5,sticky="e")

        self.last_name_entry = Entry(self)
        self.last_name_entry.grid(row=1, column=1,padx=(0,10),pady=5,sticky="ew")

        self.username_label=Label(self,text="Username")
        self.username_label.grid(row=2,column=0,padx=5,pady=5,sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=2, column=1,padx=(0,10),pady=5,sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.password_entry = Entry(self)
        self.password_entry.grid(row=3, column=1, padx=(0, 10), pady=5, sticky="ew")

        self.submit_button=Button(self,text="Submit",command=self.submit)
        self.submit_button.grid(row=4, column=0, padx=5, pady=5, sticky="e")


    def submit(self):
        first_name=self.first_name_entry.get()
        last_name=self.last_name_entry.get()
        username=self.username_entry.get()
        password=self.password_entry.get()

        result=self.user_business_logic.register(first_name,last_name,username, password)
        if result.success:
            Messagebox.showinfo(None,f"{result.mesage}")
        else:
            Messagebox.showinfo("Error",f"{result.mesage}")