"""
Practice 6
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""

def print_dec(dec_num):
    print("NUM(DEC) : ",dec_num,sep="")
        
def print_err_msg():
    err_msg = "Not Binary Number!"
    print(err_msg)

bin=input("NUM(BIN) : ")
binlist=list(bin)
binlist.reverse()
bool1=True
for num in binlist:
    if ord(num)<48 or ord(num)>49:
        print_err_msg()
        bool1=False
        break
decnum=0
if bool1:
    for i in range(len(binlist)):
        decnum+=int(binlist[i])*(2**i)
    print_dec(decnum)