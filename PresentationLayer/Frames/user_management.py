from tkinter import Frame, Label, Button,messagebox
from tkinter.ttk import Treeview
from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class UserManagement(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.row_list=[]
        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.user_business_logic = UserBusinessLogic()

        self.welcome_lable = Label(self)
        self.welcome_lable.grid(row=0, column=0, pady=10)

        self.update_button = Button(self, text="Active",command=self.active)
        self.update_button.grid(row=1, column=0, padx=(20, 0), sticky="w")

        self.delete_button = Button(self, text="Deactive",command=self.deactive)
        self.delete_button.grid(row=1, column=0, padx=(0, 20), sticky="e")

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "role", "status"))
        self.user_treeview.grid(row=2, column=0, pady=(10, 0), sticky="nsew")

        self.user_treeview.heading("#0", text="No")
        self.user_treeview.heading("#1", text="firstname")
        self.user_treeview.heading("#2", text="lastname")
        self.user_treeview.heading("#3", text="username")
        self.user_treeview.heading("#4", text="role")
        self.user_treeview.heading("#5", text="status")

    def set_current_user(self, current_user):
        self.current_user = current_user
        self.welcome_lable.config(text=f"{current_user.get_fullname()}")
        self.get_user_list()
    def lode_data(self,user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)
        self.row_list.clear()

        row_number=1
        for user in user_list:
            row=self.user_treeview.insert("","end",iid=user.id,text=str(row_number),
                                      values=(user.firstname,user.lastname,user.username,user.show_role_title(),
                                              "Active" if user.is_active else "Deactive"))
            self.row_list.append(row)
            row_number+=1


    def active(self ):
        active_user_list=self.user_treeview.selection()
        self.user_business_logic.active(self.current_user,active_user_list)
        self.get_user_list()

    def deactive(self ):
        deactive_user_list=self.user_treeview.selection()
        self.user_business_logic.deactive(self.current_user,deactive_user_list)
        self.get_user_list()

    def get_user_list(self):
        result = self.user_business_logic.get_user_list(self.current_user)
        if result.success:
            self.lode_data(result.data)
        else:
            messagebox.showinfo("Error", result.mesage)
