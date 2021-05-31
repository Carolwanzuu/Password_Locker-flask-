class User:
    """
    Class User generates new instances of users
    """

    users_list = [] #empty user list

    def __init__(self, user_name,password):

        '''
        __init__method helps define properties for our objects
    
        Args:
            user_name:New user user name.
            password:New user password.
            
        '''

        self.user_name = user_name
        self.password = password

    def add_user(self):
        '''
        save a new user instance
        '''

        User.users_list.append(self)
        
       