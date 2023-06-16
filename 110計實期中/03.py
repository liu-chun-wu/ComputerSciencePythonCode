while 1:
    word=input()
    if word=="-1":
        break
    wordlist=list(word)
    wordlist.reverse()
    maxnum=0
    for i in range(len(wordlist)):
            if ord(wordlist[i])>=65 and ord(wordlist[i])<=90:
                wordlist[i]=str(ord(wordlist[i])-55)
            elif ord(wordlist[i])>=97 and ord(wordlist[i])<=122:
                wordlist[i]=str(ord(wordlist[i])-61)
            maxnum=max(maxnum,int(wordlist[i]))
    bool1=True
    for n in range(maxnum+1,63):
        decnum=0
        for i in range(len(wordlist)):
            decnum+=int(wordlist[i])*(n**i)
        if decnum%(n-1)==0:
            print(n)
            bool1=False
            break
    if bool1:
        print("such number is impossible!")