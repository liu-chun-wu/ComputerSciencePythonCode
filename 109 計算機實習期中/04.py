s_file_name = "input.txt"
input_file = open(s_file_name, 'r')
output = open("output.txt", 'w')
input_List = []
now = 1
def cal(st):
    global now
    ret = 0
 
    while(ord(st[now])>=ord('0') and ord(st[now])<= ord('9')):
        ret*=10
        ret += int(st[now])
        now+=1
    return ret
def f(st):
    global now
    ret = 0.0
 
 
    if st[now] == '(':
        now += 1
        ret = f(st)
    if(ord(st[now])>=ord('0') and ord(st[now])<= ord('9')):
        ret = cal(st)
    if(st[now]=='+'):
        now+=1
        if(st[now]!='('):
            ret += cal(st)
        else:
            now+=1
            ret += f(st)
    if(st[now]=='-'):
        now+=1
        if(st[now]!='('):
            ret -= cal(st)
        else:
            now+=1
            ret -= f(st)
    if(st[now]=='*'):
        now+=1
        if(st[now]!='('):
            ret *= cal(st)
        else:
            now+=1
            ret *= f(st)
    if(st[now]=='/'):
        now+=1
        if(st[now]!='('):
            ret /= cal(st)
        else:
            now+=1
            ret /= f(st)
    if(st[now]==')'):
        now += 1
        return ret
 
for line in input_file:
    input_List.append([str(i)for i in line.split()])
 
 
for i in input_List:
    now = 1
    if str(f(i[0])) == i[2]:
        output.write("T\n")
    else:
        now=1
        output.write("F\n")
 
input_file.close()
output.close()