from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model, authenticate
#class LoginBackEnd(BaseBackend):
#    def authenticateLogin(self,request, idFuncionario=None,password=None, **kwargs):
#        UserModel = get_user_model()
#        try:
#            user = UserModel.objects.get(idFuncionario=idFuncionario)
#        except UserModel.DoesNotExist:
#            return None
#        else:
#            if user.check_password(password):
#                return user
#            return None