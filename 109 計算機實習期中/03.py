while 1:
    num=input()
    if num=="-1":
        break
    listnum=list(num)
    bool4=True
    bool9=True
    for word in listnum:
        if int(word)>=4:
            print("不是4進位數")
            bool4=False
            break
    if bool4:
        sum4=0
        listnum.reverse()
        for i in range(len(listnum)):
            sum4+= int(listnum[i])*(4**i)
        print(sum4)
        continue
    for word in listnum: 
        if int(word)>=9:
            print("不是9進位數")
            bool9=False
            break
    if bool9:
        sum9=0
        listnum.reverse()
        for i in range(len(listnum)):
            sum9+= int(listnum[i])*(9**i)
        print(sum9)