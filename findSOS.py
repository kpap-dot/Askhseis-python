import random
import itertools

word = "SOS"
rows = None
cols = None

def searchWord(grid,i,j,word,direction):
    flag=True
    if direction == "orizontia":
        j=j+1
        for k in range(1,len(word)):
            if j<cols and word[k]==grid[i][j]:
                j=j+1
            else:
                flag=False
                break
    elif direction == "ka8eta":
        i=i+1
        for k in range(1,len(word)):
            if i<rows and word[k]==grid[i][j]:
                i=i+1
            else:
                flag=False
                break
    elif direction == "diagonia1":
        i=i-1
        j=j+1
        for k in range(1,len(word)):
            if i>=0 and j<cols and word[k]==grid[i][j]:
                i=i-1
                j=j+1
            else:
                flag=False
                break
    elif direction == "diagonia2":
        i=i+1
        j=j-1
        for k in range(1,len(word)):
            if i>rows and j>=0 and word[k]==grid[i][j]:
                i=i+1
                j=j-1
            else:
                flag=False
                break
    if flag:
        return True
    return False       

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

positions = rows*cols

rows_index = [k for k in range(0,rows)]
cols_index = [k for k in range(0,cols)]

count=0
for a in range(1,100):
    grid=[]
    for i in range(rows):
        grid.append(['S' for k in range(cols)])
    pickO = random.sample(set(itertools.product(rows_index,cols_index)),int(positions/2))
    for i in pickO:
        grid[i[0]][i[1]]='O'

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                if searchWord(grid,i,j,word,"orizontia"):
                    count+=1
                if searchWord(grid,i,j,word,"ka8eta"):
                    count+=1
                if searchWord(grid,i,j,word,"diagonia1"):
                    count+=1
                if searchWord(grid,i,j,word,"diagonia2"):
                    count+=1

print("Mesos oros 3adwn SOS: "+str(count/100))