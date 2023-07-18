"""
Practice 4
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""

def find_prime(num):
    """
    判斷是否為質數
    從2找到n,只要存在1以外的因數,則此數為合數
    反之如果沒有找到任何1以外的因數,則為質數
    """
    if num==1:
        outputfile.write(" F\n")
        return 0
    elif num==2:
        outputfile.write(" T\n")
        return 0
    else:
        for i in range(2,num):
            if num%i==0:
                outputfile.write(" F\n")
                return 0
    outputfile.write(" T\n")
def find_factor(num):
    #從1開始到num,只要可以整除num的都是其因數
    for i in range(1,num+1):
        if num%i==0:
            outputfile.write(str(i))
            find_prime(i)

inputfile=open('Input.txt','r')
outputfile=open('Output.txt','w')  

string = inputfile.read()
listword = string.split(" ")
for i in range(len(listword)):
    outputfile.write("Number_")
    outputfile.write(str(i+1))
    outputfile.write(": ")
    outputfile.write(listword[i])
    outputfile.write("\n")
    find_factor(int(listword[i]))