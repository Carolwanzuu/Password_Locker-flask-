#!/usr/bin/env python3.8
from user import User
from credentials import Credential


def add_user(self):
    '''
    save a new user instance
    '''

    User.users_list.append(self)