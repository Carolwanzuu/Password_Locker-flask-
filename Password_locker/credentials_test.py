import unittest
from user import User
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    test class that defines test cases for the credential class behaviors
    '''

    def test_verify_user(self):
        '''
        function to test whether verify user works as expected
        '''
        self.new_user = User("Carol", "trial@01")
        self.new_user.add_user()
        userOne = User("Stella", "trial@02")
        userOne.add_user()

        for user in User.users_list:
            if user.user_name == userOne.user_name and user.password == userOne.password:
                current_user = user.user_name

        return current_user

        self.assertEqual(current_user, Credential.verify_user(userOne.username,userOne.password))


if __name__ == '__main__':
    unittest.main()