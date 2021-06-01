# Password Locker

## Built By [Carolyne Wanzuu]

## Description
Password Locker is a terminal run python application that allows users to store details such as usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Delete account credentials that are no longer in use.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password_locker.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your user name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials,  ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip


### Cloning
* In your terminal:
        
        $ git clone https://github.com/Carolwanzuu/Password_Locker-flask-.git/
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password_locker.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.8 test_run.py
        
## Technologies Used
* Python3.8


## License
This project is under the  [MIT](LICENSE) license
