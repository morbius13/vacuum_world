from random import randint

def are_ones_remaining(array):
    ones_remaining = False
    
    for row in array:
        for element in row:
            if element == 1:
                ones_remaining = True
                break 
        if ones_remaining:
            break
    return ones_remaining


Y_SIZE = 20
X_SIZE = 20

grid = []
for i in range(0, Y_SIZE):
    grid.append([])
for i in grid:
    for j in range(0, X_SIZE):
        i.append(randint(0, 1))



cur_loc = (randint(0, len(grid) - 1), randint(0, len(grid[0]) - 1))

step_count = 0

while True:
    possible_moves = [] 
    print('Current state space:')
    for i in grid:
        print(i)
    print(f'Bot is here: y: {cur_loc[0]}, x: {cur_loc[1]}')
    if grid[cur_loc[0]][cur_loc[1]] == 1:
        print("Dirt detected. Cleaning...")
        grid[cur_loc[0]][cur_loc[1]] = 0
    else:
        print("The current cell is clean.")
    if cur_loc[0] + 1 < len(grid):
        possible_moves.append((cur_loc[0] + 1, cur_loc[1]))
    if cur_loc[0] - 1 >= 0:
        possible_moves.append((cur_loc[0] - 1, cur_loc[1]))
    if cur_loc[1] + 1 < len(grid):
        possible_moves.append((cur_loc[0], cur_loc[1] + 1))
    if cur_loc[1] - 1 >= 0:
        possible_moves.append((cur_loc[0], cur_loc[1] - 1))
    if are_ones_remaining(grid) == False:
        print("No more dirt remaining. Finishing the job.")
        break
    print(f"Possible moves (y, x): {possible_moves}, choosing the best one...")
    best_moves = []
    chosen_move = None
    for i in possible_moves:
        if grid[i[0]][i[1]] == 1:
            best_moves.append(i)
    if len(best_moves) == 0:
        chosen_move = possible_moves[randint(0, len(possible_moves) - 1)]
    if len(best_moves) > 1:
        chosen_move = best_moves[randint(0, len(best_moves) - 1)]
    if len(best_moves) == 1:
        chosen_move = best_moves[0]
    print(f'Chosen move: {chosen_move}')
    print("Moving onto the next cell.\n")
    cur_loc = (chosen_move[0], chosen_move[1])
    step_count += 1
    
print(f"\nFinished in {step_count} steps")
print("Cleaned state :D")
for i in grid:
    print(i)
