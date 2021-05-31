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

        