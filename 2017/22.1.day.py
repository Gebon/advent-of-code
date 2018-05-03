tuple_sum = lambda a, b: tuple(a_n + b_n for a_n, b_n in zip(a, b))

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

direction = directions[2]

infected = set()

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

def toggle(infected, position):
    if position in infected:
        infected.remove(position)
        return False
    else:
        infected.add(position)
        return True

def turn_to_the_right(direction):
    return directions[(directions.index(direction) + 1) % len(directions)]

def turn_to_the_left(direction):
    return directions[(directions.index(direction) - 1 + len(directions)) % len(directions)]

infected_nodes_count = 0
for _ in range(10_000):
    direction = turn_to_the_right(direction) if position in infected else turn_to_the_left(direction)
    infected_nodes_count += toggle(infected, position)
    position = tuple_sum(position, direction)

print(infected_nodes_count)
