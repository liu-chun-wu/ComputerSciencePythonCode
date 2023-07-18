"""
Bonus 2
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""

def Input() :
    num = input("Please input the binary : ")
    return num

def Output( decimal, decimal_reverse ,heximal ) :
    print("Decimal:", decimal)
    print("Decimal reverse:", decimal_reverse)
    print("Heximal:", heximal)

while 1:
    bin_num=Input()
    if bin_num=="-1":
        break
    binlist=list(bin_num)
    bool1=False
    for num in binlist:
        if num!="0" and num!="1":
            print("Input number is not binary")
            bool1=True
            break
    if bool1:
        continue
    binlist.reverse()
    if binlist[len(binlist)-1]=="1":
        for i in range(len(binlist)):
            if binlist[i]=="1":
                binlist[i]="0"
            else :
                binlist[i]="1"
            if i==0:
                binlist[i]=str(int(binlist[i])+1)
        carry=0
        for i in range(len(binlist)):
            if carry:
                binlist[i]=str(int(binlist[i])+1)
                carry=0
            if binlist[i]=="2":
                carry=1
                binlist[i]="0"
    decimal=0
    for i in range(len(binlist)):
        decimal+=int(binlist[i])*(2**i)
    declist=list(str(decimal))
    declist.reverse()
    decimal_reverse=int("".join(declist))
    hexlist=[]
    decimal_temp=decimal
    while decimal_temp!=0:
        if decimal_temp%16<10:
            hexlist.append(str(decimal_temp%16))
        else:
            hexlist.append(chr(decimal_temp%16+87))
        decimal_temp=decimal_temp//16
    hexlist.reverse()
    heximal="".join(hexlist)
    Output(decimal, decimal_reverse, heximal)