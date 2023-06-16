"""
Practice 2
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A
"""
while 1:
    password=input("Please enter your password: ")
    if password=="exit":
        exit()
    if len(password)<6 or len(password)>10:
        print('Password should contain 6 to 10 characters, try again or type "exit" to leave.')
        continue
    bool1 = True
    for i in range(len(password)):
        if 65<=ord(password[i])<=90:
            bool1 = False
            break
    if bool1:
        print('Password should contain at least one upper-case alphabetical character, try again or type "exit" to leave.')      
        continue          
    bool2=True
    for i in range(len(password)):
        if 48<=ord(password[i])<=57:
            bool2=False
            break
    if bool2:
        print('Password should contain at least one number, try again or type "exit" to leave.')
        continue
    print("Password is valid.")
    break