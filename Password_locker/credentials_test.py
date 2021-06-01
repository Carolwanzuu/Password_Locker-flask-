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


    def setUp(self):
        '''
        function to create an accounts credentials before each test
        '''
        self.new_credential = Credential("Stella", "facebook","trial@02")

    def test_init(self):
        '''
        This checks whether initialization of credentials was successful
        '''
        self.assertEqual(self.new_credential.user_name, "Stella")
        self.assertEqual(self.new_credential.site_name, "facebook")
        self.assertEqual(self.new_credential.password, "trial@02")


    def test_save_credentials(self):
        '''
        tests whether credentials are saved
        '''
        self.new_credential.save_credentials()
        twitter = Credential("Charles", "twitter", "trial@03")
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)  

    def test_find_by_site(self):
        '''
        tests to check if we can get users based on the name of the site
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("Agnes", "Twitter", "trial@04")
        test_credential.save_credentials()
        credential_exists = Credential.find_by_site_name("Twitter")
		self.assertEqual(credential_exists.password,test_credential.password)


if __name__ == '__main__':
    unittest.main()