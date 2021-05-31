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
        self.new_user = User("Carol", "Wanzuu", "0387405923","carol@gmail.com")

    def test_init(self):
        '''
        tests if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Carol")
        self.assertEqual(self.new_user.last_name,"Wanzuu")
        self.assertEqual(self.new_user.phone_number,"0387405923")
        self.assertEqual(self.new_user.email,"carol@gmail.com")

if __name__ == '__main__':
    unittest.main()