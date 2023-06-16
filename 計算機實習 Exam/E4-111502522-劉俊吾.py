"""
Exam 4
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""
def open_file(file_name):
    inputfile=open(file_name,"r")
    for line in inputfile:
        return line
def check_number(num):
    checklist=list(num)
    for word in checklist:
        if word=="0":
            return False
    for i in range(len(checklist)):
        for j in range(len(checklist)):
            if i!=j and checklist[i]==checklist[j]:
                return False
    if num.isdigit() and len(num)==4 :
        return True
    else:
        return False
def cmp_number(ans_num,guess_num):
    anslist=list(str(ans_num))
    guesslist=list(str(guess_num))
    countA=0
    countB=0
    for i in range(len(anslist)):
        for j in range(len(guesslist)):
            if i==j and anslist[i]==guesslist[j]:
                countA+=1
            elif i!=j and anslist[i]==guesslist[j]:
                countB+=1
    return countA,countB

ans = open_file("E4_input.txt")
if check_number(ans)==False:
    print("answer file error")
    exit(0)
while 1:
    guess=input()
    if check_number(guess):
        counta,countb=cmp_number(ans,guess)
        if counta==4 :
            break
        else:
            print(counta,"A",countb,"B")
    else:
        print("input error")
