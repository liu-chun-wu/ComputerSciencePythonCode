"""
Practice 8
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""
def readfile():
    input_file=open("input.txt","r")
    line=input_file.read()
    input_file.close()
    inputlist=line.split()
    return inputlist
inputlist=readfile()
for i in range(len(inputlist)-1,1-1,-1):
    for j in range(i):
        count=j
        if int(inputlist[count])>int(inputlist[count+1]):
            inputlist[count],inputlist[count+1]=inputlist[count+1],inputlist[count]
print(inputlist)