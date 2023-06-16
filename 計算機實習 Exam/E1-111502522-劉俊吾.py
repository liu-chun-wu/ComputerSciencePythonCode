"""
Exam 1
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""

def open_file(file_name):
    inputlist=[]
    inputfile=open(file_name,"r")
    for line in inputfile:
        inputlist=line.split()
    return inputlist
newlist=[]
oldlist=open_file("E1_input3.txt")
sum=0
for i in range(len(oldlist)):
    sum+=int(oldlist[i])
    newlist.append(sum)
print("new_list = ",newlist)