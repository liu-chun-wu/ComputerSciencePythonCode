"""
Bonus 1
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""
invoice_file=open("invoice.txt","r")
num_file=open("num.txt","r")
count=[0,0,0,0,0,0,0,0,0]
#特別獎 特獎 頭獎 二獎 三獎 四獎 五獎 六獎 沒中獎
def Output(count,total):
    print('特別獎：', count[0])
    print('特獎：', count[1])
    print('頭獎：', count[2])
    print('二獎：', count[3])
    print('三獎：', count[4])
    print('四獎：', count[5])
    print('五獎：', count[6])
    print('六獎：', count[7])
    print('沒中獎：', count[8])
    print(total)

numlist=[]
for num in num_file:
    numlist.append(num)
for invoice in invoice_file:
    #特別獎 特獎
    if numlist[0][0:8]==invoice[0:8]:
        count[0]+=1
    elif numlist[1][0:8]==invoice[0:8]:
        count[1]+=1
    #第一列頭獎
    elif numlist[2][0:8]==invoice[0:8]:
        count[2]+=1
    elif numlist[2][1:8]==invoice[1:8]:
        count[3]+=1
    elif numlist[2][2:8]==invoice[2:8]:
        count[4]+=1
    elif numlist[2][3:8]==invoice[3:8]:
        count[5]+=1
    elif numlist[2][4:8]==invoice[4:8]:
        count[6]+=1
    elif numlist[2][5:8]==invoice[5:8]:
        count[7]+=1
    #第二列頭獎
    elif numlist[3][0:8]==invoice[0:8]:
        count[2]+=1
    elif numlist[3][1:8]==invoice[1:8]:
        count[3]+=1
    elif numlist[3][2:8]==invoice[2:8]:
        count[4]+=1
    elif numlist[3][3:8]==invoice[3:8]:
        count[5]+=1
    elif numlist[3][4:8]==invoice[4:8]:
        count[6]+=1
    elif numlist[3][5:8]==invoice[5:8]:
        count[7]+=1
    #第三列頭獎
    elif numlist[4][0:8]==invoice[0:8]:
        count[2]+=1
    elif numlist[4][1:8]==invoice[1:8]:
        count[3]+=1
    elif numlist[4][2:8]==invoice[2:8]:
        count[4]+=1
    elif numlist[4][3:8]==invoice[3:8]:
        count[5]+=1
    elif numlist[4][4:8]==invoice[4:8]:
        count[6]+=1
    elif numlist[4][5:8]==invoice[5:8]:
        count[7]+=1
    #增開三個六獎
    elif numlist[5][0:3]==invoice[5:8]:
        count[7]+=1
    elif numlist[6][0:3]==invoice[5:8]:
        count[7]+=1
    elif numlist[7][0:3]==invoice[5:8]:
        count[7]+=1
    #沒有中獎
    else:
        count[8]+=1
total=count[0]*10000000+count[1]*2000000+count[2]*200000+count[3]*40000\
    +count[4]*10000+count[5]*4000+count[6]*1000+count[7]*200
Output(count, total)

invoice_file.close()
num_file.close()
