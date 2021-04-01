import io
import re
"""
      Student:Ngan Hoang
      Module: gladysUserLogin
      Description: This module does log the users in and tell if the email valide or not.
"""

def login():
        
        validEmail = False
        while (not validEmail):
                emailAddress = input('Enter login:')
                password = input('Enter password:')

                missingAt = '@' not in emailAddress
                missingDot = '.' not in emailAddress
                missingCom = 'com' not in emailAddress
                if missingAt or missingDot or missingCom:
                        print('ERROR: User login is not an mail address')
                else:
                        validEmail = True

        return emailAddress