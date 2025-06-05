def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            pixel = "*" if elem == 1 else " "
            print(pixel, end=" ")
        print()
    
row1 = [5,6,7]
row2 = [1,2,3]

matrix = [row1, row2]

screen = [
    [0,1,0],
    [0,1,0],
    [0,1,1]
]

print_matrix(screen)
    
    
    