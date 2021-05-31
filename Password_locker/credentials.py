from user import User


class Credential:
    """
    Class Credential generates new instances of credentials
    """

    credentials_list = [] 
    user_credentials_list = []
    @classmethod

    def verify_user(cls, user_name, password):
        '''
        method verifies if the name and password entered match with users_list info
        '''
    
        current_user = ''
        for user in User.users_list:
            if(user.user_name == user_name and user.password == password):
                 return True
            else:
                print('Invalid username or password..')
