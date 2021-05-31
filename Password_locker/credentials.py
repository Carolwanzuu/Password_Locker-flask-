from user import User
import string
import random

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


    def __init__(self, user_name, site_name,password):
        '''
        method defines properties for each user object
        '''

        #instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.password = password

    def save_credentials(self):
         '''
        save a new credentials instance
        '''

         Credential.credentials_list.append(self)

    def generate_password(size = 10,  char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        function to generate a password
        '''

        gen_password = ''.join(random.choice(char) for _ in range(size))
        return gen_password