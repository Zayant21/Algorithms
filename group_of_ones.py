def checksublist(sublist, list):
    if sublist in list:
        return True
    return False

def find1s(grid):
    total_group = 0;
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and checksublist([row,col], visited) == False:
                total_ones = check_nighbours(grid ,row,col)
                total_group = total_group + 1
    return total_group

def check_nighbours(grid,row,col):
    if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
        return 0
    if grid[row][col] == 0:
        return 0
    cell_count = 1
    grid[row][col] = 0
    
    for r in range(row-1 , row+2):
        for c in range(col-1 , col+2):
            if r != row or c != col:
                visited.append([r,c])
                cell_count = check_nighbours(grid,r,c)
    

visited = []
grid = [[1,0,1,1],
        [0,0,0,1],
        [1,0,0,0],
        [0,1,1,1]]
print( 'Groups of 1s ', find1s(grid))