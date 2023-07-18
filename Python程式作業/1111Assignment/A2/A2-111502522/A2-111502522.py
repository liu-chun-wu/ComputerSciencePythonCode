"""
Assignment 2
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""

while 1:
    password1=input("Please enter your password: ")
    if password1=="exit":
        exit()
    password2=input("Please enter your password again: ")
    if password1 != password2:
        print('Password settings are not consistent, try again or type "exit" to leave.')
        continue
    elif len(password1)<6 or len(password1)>10:
        print('Password should contain 6 to 10 characters, try again or type "exit" to leave.')
        continue
    bool1 = True
    for i in range(len(password1)):
        if 65<=ord(password1[i])<=90:
            bool1 = False
            break
    if bool1:
        print('Password should contain at least one upper-case alphabetical character, try again or type "exit" to leave.')      
        continue          
    bool2 = True
    for i in range(len(password1)):
        if 97<=ord(password1[i])<=122:
            bool2=False
            break
    if bool2:
        print('Password should contain at least one lower-case alphabetical character, try again or type "exit" to leave')
        continue
    bool3=True
    for i in range(len(password1)):
        if 48<=ord(password1[i])<=57:
            bool3=False
            break
    if bool3:
        print('Password should contain at least one number, try again or type "exit" to leave.')
        continue
    bool4=True
    for i in range(len(password1)):
        if 32<=ord(password1[i])<=47 or 58<=ord(password1[i])<=64 or 91<=ord(password1[i])<=96 or 123<=ord(password1[i])<=127:
            bool4=False
            break
    if bool4:
        print('Password should contain at least one special character, try again or type "exit" to leave.')
        continue
    if list(password1)==list(reversed(password1)):
        print('Symmetric password is not allowed, try again or type "exit" to leave.')
        continue
    print("Password is valid.")
    break