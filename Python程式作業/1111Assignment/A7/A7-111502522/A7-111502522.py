"""
Assignment 7
Name: 劉俊吾
Student Number: 111502522
Course 2022-CE1001-A
"""
def get_maze():
    f = open('input.txt', 'r')
    maze = []
    for lines in f:
        maze.append(lines.split())
    f.close()
    return maze
maze=get_maze()
def find_path(maze,y,x):
    ans=0
    if y==5 and x==5:
        ans=1
    else:
        if maze[y][x+1]=="1":
            ans+=find_path(maze,y,x+1)
        if maze[y+1][x]=="1":
            ans+=find_path(maze,y+1,x)
    return ans
print(find_path(maze,1,1))
