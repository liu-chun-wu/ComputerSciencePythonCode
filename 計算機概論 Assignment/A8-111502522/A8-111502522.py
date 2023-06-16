"""
Assignment 8
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""
def readfile():
    input_file=open("input.txt","r")
    line=input_file.read()
    input_file.close()
    inputlist=line.split()
    return inputlist
inputlist_origin=readfile()
inputlist_sort=readfile()
count=0
for i in range(len(inputlist_sort)-1,1-1,-1):
    count+=1
    for j in range(i):
        postion=j
        if int(inputlist_sort[postion])>int(inputlist_sort[postion+1]):
            inputlist_sort[postion],inputlist_sort[postion+1]=inputlist_sort[postion+1],inputlist_sort[postion]
    print("第",count,"次",inputlist_sort)
print("原資料: ",inputlist_origin)