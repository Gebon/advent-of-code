from time import sleep

directions = {
    'up': (0, -1),
    'down': (0, 1),
    'right': (1, 0),
    'left': (-1, 0)
}

next_direction = {
    'up': 'left',
    'down': 'right',
    'right': 'up',
    'left': 'down'
}

neighbors_directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def sum_tuples(a, b):
    return a[0] + b[0], a[1] + b[1]

def get_neighbors(position):
    return (sum_tuples(position, direction) for direction in neighbors_directions)

def grid_generator():
    current_position = (0, 0)
    grid = {}
    grid[current_position] = 1
    direction_name = 'right'
    direction = directions[direction_name]
    while True:
        yield grid[current_position]
        current_position = sum_tuples(current_position, direction)
        if sum_tuples(current_position, directions[next_direction[direction_name]]) not in grid:
            direction_name = next_direction[direction_name]
            direction = directions[direction_name]
        grid[current_position] = sum((grid[neighbor] for neighbor in get_neighbors(current_position) if neighbor in grid))

for num in grid_generator():
    if num > 265149:
        print(num)
        break
