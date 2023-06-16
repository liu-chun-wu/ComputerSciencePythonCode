"""
Exam 2
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""
def open_file(file_name):
    list1=[]
    list2=[]
    count=0
    inputfile=open(file_name,"r")
    for line in inputfile:
        count+=1
        if count==1:
            list1=line.split()
        elif count==2:
            list2=line.split()
    return list1,list2
def search_index(inputlist,target):
    count=0
    for i in range(len(inputlist)):
        if target.isdigit():
            if int(target)>int(inputlist[i]):
                count+=1 
        if target.isalpha():
            if ord(target)>ord(inputlist[i]):
                count+=1 
        if target == inputlist[i]:
            return i
    else:
        return count

list1,list2=open_file("E2_input.txt")
target=input("輸入 : ")
if target.isdigit():
    place=search_index(list2, target)
    print("Search list : ",2)
    print("Index : ",place)
else:
    place=search_index(list1, target)
    print("Search list : ",1)
    print("Index : ",place)