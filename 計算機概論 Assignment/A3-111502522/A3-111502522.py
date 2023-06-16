"""
Assignment 3
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""

inputfile=open('Input.txt','r')
outputfile=open('Output.txt','w')

def  isPrime(count):
    """
    判斷是否為質數
    從2找到n,只要存在1以外的因數,則此數為合數
    反之如果沒有找到任何1以外的因數,則為質數
    """
    if count==1:
        outputfile.write("1")
        return 0
    elif count==2:
        outputfile.write("Y")
        return 0
    else:
        for i in range(2,count):
            if count%i==0:
                outputfile.write("N")
                return 0
    outputfile.write("Y")
            
def CreatePyramid(num):
    #印金字塔
    count=0
    #計數器
    #我是從1開始數的因為比較好寫
    for i in range(1,num+1,1):
        for j in range(num-i,0,-1):
            outputfile.write(" ")
        for k in range(1,i*2,1):
            count+=1
            #每印一次數字,計數器+1，並把加1後的數丟到判斷質數的函式
            isPrime(count)
        if i !=num:
            outputfile.write("\n")

num=inputfile.read()
num=int(num)
#輸入為字串,要轉成整數
CreatePyramid(num)