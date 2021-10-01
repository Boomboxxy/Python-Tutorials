"""
Insert your username : andres
Insert your email : andres@rodriguez.com
Insert your password : andres123#

Welcome to the System.
OR
Invalid Credentials.
"""

correct_username = "kaustubh"
correct_email = "kaustubh@wankhede.com"
correct_password = "KaustubhKWankhede"

username = input('Insert your username\t:\t')
email = input('Insert your email\t:\t')
password = input('Insert your password\t:\t')

if username == correct_username and email == correct_email and password == correct_password:
    print('Welcome to the system.')
else:
    print('Invalid Credentials.')