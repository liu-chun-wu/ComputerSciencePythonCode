string = input()
listword=string.split()
listword1=list(listword[0])
listword2=list(listword[1])
print("OR: ",end="")
for i in range(len(listword1)):
    if listword1[i]=="1" or listword2[i]=="1":
        print(1,end="")
    else:
        print(0,end="")
print()
print("AND: ",end="")
for i in range(len(listword1)):
    if listword1[i]=="1" and listword2[i]=="1":
        print(1,end="")
    else:
        print(0,end="")
print()
print("XOR: ",end="")
for i in range(len(listword1)):
    if listword1[i]!=listword2[i]:
        print(1,end="")
    else:
        print(0,end="")
print()