import unittest
from unittest.case import TestCase
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for user class behaviors

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Method to run before each test cases
        '''
        self.new_user = User("Carol", "trial@01")

    def test_init(self):
        '''
        tests if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Carol")
        self.assertEqual(self.new_user.password,"trial@01")
        

    def tearDown(self):
        '''
        tearDown method cleans up after each test case has run
        '''
        User.users_list = []

    def test_add_user(self):
        '''
        test to check if new user is added
        '''

        self.new_user.add_user()
        self.assertEqual(len(User.users_list),1)

    

if __name__ == '__main__':
    unittest.main()