class User:
    """
    Class User generates new instances of users
    """

    user_list = [] #empty user list

    def __init__(self, user_name,password):

        '''
        __init__method helps define properties for our objects
    
        Args:
            user_name:New user user name.
            password:New user password.
            
        '''

        self.user_name = user_name
        self.password = password
       