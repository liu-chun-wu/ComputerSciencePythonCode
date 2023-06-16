"""
Exam 3
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1003-A 
"""
def open_file(file_name):
    timelist=[]
    inputfile=open(file_name,"r")
    for line in inputfile:
        timelist.append(line.split())
    return timelist
def bool_finish(inputlist):
    start_hr=int(inputlist[0])
    start_min=int(inputlist[1])
    end_hr=int(inputlist[2])
    end_min=int(inputlist[3])
    start_min_sum=start_hr*60+start_min
    end_min_sum=end_hr*60+end_min
    if start_min_sum+int(inputlist[4])>end_min_sum:
        return "No"
    else:
        return "Yes"

timelist = open_file("E3_input5.txt")
input_time=int("".join(timelist[0]))
for  i  in range(1,input_time+1):
    print(bool_finish(timelist[i]))

