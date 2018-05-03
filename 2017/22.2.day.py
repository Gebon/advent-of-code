tuple_sum = lambda a, b: tuple(a_n + b_n for a_n, b_n in zip(a, b))

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

direction = directions[2]

infected = set()
weakened = set()
falgged = set()

width = height = 0

for i, row in enumerate('''..####.###.##..##....##..
.##..#.###.##.##.###.###.
......#..#.#.....#.....#.
##.###.#.###.##.#.#..###.
#..##...#.....##.#..###.#
.#..#...####...#.....###.
##...######.#.###..#.##..
###..#..##.###....##.....
.#.#####.###.#..#.#.#..#.
#.#.##.#.##..#.##..#....#
..#.#.#.#.#.##...#.####..
##.##..##...#..##..#.####
#.#..####.##.....####.##.
..####..#.#.#.#.##..###.#
..#.#.#.###...#.##..###..
#.####.##..###.#####.##..
.###.##...#.#.#.##....#.#
#...######...#####.###.#.
#.####.#.#..#...##.###...
####.#.....###..###..#.#.
..#.##.####.#######.###..
#.##.##.#.#.....#...#...#
###.#.###..#.#...#...##..
##..###.#..#####.#..##..#
#......####.#.##.#.###.##'''.split('\n')):
    for j, item in enumerate(row):
        if item == '#':
            infected.add((i, j))
    width = max(width, len(row))
    height = i + 1

position = (height // 2, width // 2)

def toggle(position):
    if position in infected:
        infected.remove(position)
        falgged.add(position)
    elif position in falgged:
        falgged.remove(position)
    elif position in weakened:
        weakened.remove(position)
        infected.add(position)
        return True
    else:
        weakened.add(position)
    return False

def is_clean(position):
    return position not in weakened and position not in infected and position not in falgged

def turn_to_the_right(direction):
    return directions[(directions.index(direction) + 1) % len(directions)]

def turn_to_the_left(direction):
    return directions[(directions.index(direction) - 1 + len(directions)) % len(directions)]

def reverse(direction):
    return directions[(directions.index(direction) + 2) % len(directions)]    

def get_next_direction(position, direction):
    if position in weakened:
        return direction
    if position in infected:
        return turn_to_the_right(direction)
    if position in falgged:
        return reverse(direction)
    return turn_to_the_left(direction)


infected_nodes_count = 0
for _ in range(10_000_000):
    direction = get_next_direction(position, direction)
    infected_nodes_count += toggle(position)
    position = tuple_sum(position, direction)

print(infected_nodes_count)
