def asciiart(list):
    current_row = 0
    current_col = 0
    output_string = ""

    while current_col < len(list[0]):
        while current_row < len(list):
            output_string += list[current_row][current_col]
            current_row += 1
        current_row = 0
        output_string += "\n"
        current_col += 1
    print(output_string)
        
grid = [
    ['.','.','.','.','.','.'],
    ['.','0','0','.','.','.'],
    ['0','0','0','0','.','.'],
    ['0','0','0','0','0','.'],
    ['.','0','0','0','0','0'],
    ['0','0','0','0','0','.'],
    ['0','0','0','0','.','.'],
    ['.','0','0','.','.','.'],
    ['.','.','.','.','.','.']
]

asciiart(grid)
