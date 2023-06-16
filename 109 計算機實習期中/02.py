num=eval(input())
for i in range(1,num+1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for j in range(1,2*i-1+1):
        print("*",end="")
    print()
for i in range(1,num):
    for j in range(1,int((num+1)/2+1)):
        print(" ",end="")
    for j in range(1,num-2+1):
        print("*",end="")
    print()
"""
3-> 2 * " " + 1 * "*" 
5-> 3 * " " + 3 * "*" 
7-> 4 * " " + 5 * "*" 
n->(n+1)/2 + (n-2) 
"""