def treeMaker():
    rows = 10
    cols = 10
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = i * cols + j + 1  # Example: populate with sequential numbers
            row.append(value)
        matrix.append(row)

    mazeTree = {} 

    for i in range(10):
        for j in range(10):
            if (i != 0 and i != 9) and (j != 0 and j != 9): #non corner elements
                mazeTree[matrix[i][j]] = [matrix[i+1][j], matrix[i][j+1], matrix[i-1][j], matrix[i][j-1]]
            elif (i == 0 and j<9): #top row elements
                mazeTree[matrix[i][j]] = [matrix[i+1][j], matrix[i][j+1], matrix[i][j-1]]
            elif (i == 9 and j<9): # bottom row elements
                mazeTree[matrix[i][j]] = [matrix[i-1][j], matrix[i][j+1], matrix[i][j-1]]
            elif (i < 9 and j==0): # left side elements 
                mazeTree[matrix[i][j]] = [matrix[i][j+1], matrix[i+1][j], matrix[i-1][j]]
            elif (i < 9 and j==9): # right side elements 
                mazeTree[matrix[i][j]] = [matrix[i][j-1], matrix[i+1][j], matrix[i-1][j]]


    #init the corners 
    mazeTree[matrix[0][0]] = [matrix[1][0], matrix[0][1]]
    mazeTree[matrix[9][9]] = [matrix[8][9], matrix[9][8]]
    mazeTree[matrix[0][9]] = [matrix[0][8], matrix[1][9]]
    mazeTree[matrix[9][0]] = [matrix[8][9], matrix[9][8]]
    
    return mazeTree