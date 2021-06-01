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

    def verify_user(user_name, password):
        '''
        function to verify existance of a user
        '''
        verify_user = Credential.verify_user(user_name, password)
        return verify_user


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

        elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credentials(create_credential(user_name,site_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name}  - Password: {password}')
						print(' ')
                    elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')	

    else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')
					