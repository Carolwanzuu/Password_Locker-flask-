#!/usr/bin/env python3.8
from user import User
from credentials import Credential

    def create_user(user_name, password):
        '''
        function to create new user
        '''
        new_user = User(user_name, password)
        return new_user





    def add_user(self):
        '''
        save a new user instance
        '''

        User.users_list.append(self)


    def generate_password():
        '''
        function to generate a password automatically
        '''
        generate_password = Credential.generate_password()
        return generate_password


    def create_credential(user_name,site_name,password):
        '''
        Function to create a new credential
        '''
        new_credential=Credential(user_name,site_name,password)
        return new_credential

    def save_credentials(self):
            '''
            save a new credentials instance
            '''
            Credential.save_credentials()

    
def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			user_name = input('Enter your user name - ').strip()
			password = input('Enter your password - ').strip()
			add_user(create_user(user_name,password))
			print(" ")
			print(f'New Account Created for:{user_name} using password: {password}')
