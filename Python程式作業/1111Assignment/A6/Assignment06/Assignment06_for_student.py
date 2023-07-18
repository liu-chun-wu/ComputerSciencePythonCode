'''
Assignment 06
Name: 
Student Number: 
Course 2022-CE1001-班級
'''

def print_dec(dec_num):
    print("NUM(DEC) : {}".format(dec_num))
    
def print_oct(oct_num):
    print("NUM(OCT) : {}".format(oct_num)) #format function will replace the "{}" with given variables, you can google it for the detail
    
def print_err_msg():
    err_msg = "Not Binary Number!"
    print(err_msg)
    
while 1:
    number = input("NUM(BIN) : ")
    # write your code form here...
    
    # if number equal to "-1" then break the while loop.
    
    # if input is not binary number, like "abc","7789", use print_err_msg() to print msg.
    
    # do not use "int(number,2)"
    
    # ...to here