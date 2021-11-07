def street_fighter_selection(fighters, initial_position, moves):
    row, col = initial_position 
    solution = []

    move = {
        'up': lambda row: row if row == 0 else row - 1,
        'down': lambda row: row if row == 1 else row + 1,
        'right': lambda col: (col + 1)%6,
        'left': lambda col: (col - 1)%6
    }
    
    for next_move in moves:
        if next_move in ["left", "right"]:
            col = move[next_move](col)
        else:
            row = move[next_move](row)
        solution.append(fighters[row][col])
    return [] if len(moves) == 0 else solution
