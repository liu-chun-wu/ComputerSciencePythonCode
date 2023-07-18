"""
Assignment 3
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""

inputfile=open('input.txt','r')
outputfile=open('output.txt','w')

def CreatePyramid(num):
    count=0
    for i in range(1,num+1,1):
        for j in range(num-i,0,-1):
            outputfile.write(" ")
        for k in range(1,i*2,1):
            count+=1
            isPrime(count)
        if i !=num:
            outputfile.write("\n")
        
def  isPrime(count):
    bool1=True
    if count==1:
        outputfile.write("1")
    elif count==2:
        outputfile.write("Y")
    else:
        for i in range(2,count):
            if count%i==0:
                outputfile.write("N")
                bool1=False
                break
        if bool1:
            outputfile.write("Y")

num=inputfile.read()
num=int(num)
CreatePyramid(num)