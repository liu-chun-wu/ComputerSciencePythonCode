"""
Assignment 4
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""

inputfile = open('Input.txt','r')
inputlist=[]
for line in inputfile:
    inputlist.append(line.split())
def num_exist(num):
    for i in range(len(inputlist)):
        if inputlist[i][0]=="Number_"+num:
            return True
    return False
def count_factor(num):
    for i in range(len(inputlist)):
        if inputlist[i][0]=="Number_"+num:
            return len(inputlist[i])-1
def count_prime(num):
    count=0
    for i in range(len(inputlist)):
        if inputlist[i][0]=="Number_"+num:
            print(inputlist[i])
            for j in range(1,len(inputlist[i])):
                print(inputlist[i][j])
                if inputlist[i][j] == "1":
                    continue
                elif inputlist[i][j]=="2":
                    count+=1
                else:
                    bool1=True
                    for k in range(2,int(inputlist[i][j])):
                        print(k)
                        if int(inputlist[i][j])%k==0:
                            bool1=False
                            break
                    if bool1:
                        count+=1
                print(count,"this is count")
            return count
while 1:
    num=input("Input the number to check exist or exit : ")
    if num=="exit":
        break
    if num_exist(num):
        factor_num=count_factor(num)
        prime_num=count_prime(num)
        print("Number_",num," exists in the document and the number of factor is ",factor_num," and the number of prime is ",prime_num,sep="")
    else:
        print('Number_',num,' is not exist, please input a new number or input "exit" to leave program',sep="")
        print('Please input the next number or input "exit" to leave')
inputfile.close()
