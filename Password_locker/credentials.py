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
    
