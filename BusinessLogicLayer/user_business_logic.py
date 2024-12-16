from Common.ResponseModel.response import Response
from DataAccessLayer.UserDataAccess import UserDataAccess
from Common.Decorators.performance_decorator import performance_logger_decorator
class UserBusinessLogic:
    def __init__(self):
        self.user_data_access=UserDataAccess()
    @performance_logger_decorator
    def login(self,username,password):
        if len(username)<3 or len(password)<3:
            return Response(False,"Invalid Response",None)
        user=self.user_data_access.get_user(username,password)
        if not user:
            return Response(False,"Invalid username or password",None)
        if user.is_active:
            return Response(True,None,user)
        else:
            return Response(False,"Your account is deactive",None)

    @performance_logger_decorator
    def register(self,firstname,lastname,username,password):
        if len(firstname)<1 or len(lastname)<1 or len(username)<1 or len(password)<1:
            return Response(False,"Please complete the options",None)
        if len(username)<3 or len(password)<3:
            return Response(False,"User and Pass should not be less than 3 characters",None)
        user=self.user_data_access.check_username(username)
        if user:
            return Response(False,"It is a recurring username",None)
        self.user_data_access.insert_user(firstname,lastname,username,password)
        return Response(True,"Registration was successful",None)

    @performance_logger_decorator
    def get_user_list(self,current_user):
        if not current_user.is_active:
            return Response(False,"Your account is deactive",None)
        if current_user.show_role_title() !="Admin":
            return Response(False,"Access Denied",None)
        user_list=self.user_data_access.get_user_list(current_user.id)
        return Response(True,None,user_list)

    @performance_logger_decorator
    def active(self,current_user,user_id_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive", None)
        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied", None)
        for user_id in user_id_list:
            self.user_data_access.update_is_active(user_id,1)

    @performance_logger_decorator
    def deactive(self,current_user,user_id_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive", None)
        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied", None)
        for user_id in user_id_list:
            self.user_data_access.update_is_active(user_id, 0)
