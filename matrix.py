def zero_out(matrix):
    for i,row in enumerate(matrix):
        for j,col in enumerate(row):
            if col == 0:
                origin = i,j
                break

    maxRow=len(matrix)
    maxCol=len(matrix[0])

    row,col=origin


    for x in range(maxRow):
        matrix[x][col]=0

    for y in range(maxCol):
        matrix[row][y]=0


    return matrix


matrix = [ ['A', 'B', 'C', 'D'], ['E', 'F', 0, 'H'], ['I', 'J', 'K', 'L'] ]

new=zero_out(matrix)

for x in new:
    print(x)