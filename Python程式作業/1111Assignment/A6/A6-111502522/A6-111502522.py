"""
Assignment 6
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""
def print_dec(dec_num):
    print("NUM(DEC) : {}".format(dec_num))
    
def print_oct(oct_num):
    print("NUM(OCT) : {}".format(oct_num)) 
    
def print_err_msg():
    err_msg = "Not Binary Number!"
    print(err_msg)

while 1:
    bin=input("NUM(BIN) : ")
    if bin=="-1":
        break
    binlist=list(bin)
    bool1=True
    for i in binlist:
        if i!="0":
            bool1=False
            break
    if bool1:
        print_dec(0)
        print_oct(0)
        continue
    binlist.reverse()
    bool1=True
    for num in binlist:
        if ord(num)<48 or ord(num)>49:
            print_err_msg()
            bool1=False
            break
    decnum=0
    octlist=[]
    if bool1:
        for i in range(len(binlist)):
            decnum+=int(binlist[i])*(2**i)
        print_dec(decnum)
        while decnum!=0:
            octlist.append(str(decnum%8))
            decnum=int(decnum/8)
        octlist.reverse()
        octnum="".join(octlist)
        print_oct(octnum)
