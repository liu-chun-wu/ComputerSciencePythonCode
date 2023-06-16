"""
Assignment 5
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""
def split_info( input_list ) :
    return_list = []
    for i in range(int(len(input_list))):
        if i%5==0:
            return_list.append(input_list[i:i+5])
    return return_list

def grading_system( student_list ) :
    return_str = ''
    Chinese_score = int(student_list[1])
    English_score = int(student_list[2])
    Math_score = int(student_list[3])
    Science_score =  int(student_list[4])
    if Chinese_score >= 12 and English_score >= 12 and Math_score >=8 and Science_score >= 12:
        return_str="Hello "+ student_list[0] + ", welcome to NCU CSIE!"
    else : 
        return_str="Sorry, " + student_list[0] + " can't enter NCU CSIE."

    return return_str # should be: "Hello "+ name + ", welcome to NCU CSIE!"  or "Sorry, " + name + " can't enter NCU CSIE." 

def find_grade( s_list, name, subject ) :
    return_str = ''
    return_str="Error"
    for i in range(len(s_list)):
        if s_list[i][0]==name:
            if subject=="chinese":
                return_str=s_list[i][1]
            elif subject=="english":
                return_str=s_list[i][2]
            elif subject=="math":
                return_str=s_list[i][3]
            elif subject=="science":
                return_str=s_list[i][4]      
    return return_str 
input_list=[]
temp_list=[]
s_file_name = open('score.txt','r')
c_file_name = open('cmd.txt','r')
outputfile = open('output.txt','w')
for line in s_file_name:
    input_list.extend(line.split())
input_list = split_info( input_list )
for line in input_list:
    student_list=line
    outputfile.write(grading_system( student_list ))
    outputfile.write("\n")
for line in c_file_name:
    temp_list=line.split()
    name=temp_list[0]
    subject=temp_list[1]
    outputfile.write(find_grade( input_list, name, subject ))
    outputfile.write("\n")
