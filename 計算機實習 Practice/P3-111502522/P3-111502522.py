"""
Practice 3
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""

inputfile=open('input.txt','r')
outputfile=open('output.txt','w')

def CreatePyramid(num):
    for i in range(1,num+1,1):
        for j in range(num-i,0,-1):
            outputfile.write(" ")
        for k in range(1,i*2,1):
            outputfile.write("*")
        if i !=num:
            outputfile.write("\n")

num=inputfile.read()
num=int(num)
CreatePyramid(num)

