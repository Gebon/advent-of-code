from collections import defaultdict

puzzle = '''0: 5
1: 2
2: 3
4: 4
6: 6
8: 4
10: 6
12: 10
14: 6
16: 8
18: 6
20: 9
22: 8
24: 8
26: 8
28: 12
30: 12
32: 8
34: 8
36: 12
38: 14
40: 12
42: 10
44: 14
46: 12
48: 12
50: 24
52: 14
54: 12
56: 12
58: 14
60: 12
62: 14
64: 12
66: 14
68: 14
72: 14
74: 14
80: 14
82: 14
86: 14
90: 18
92: 17'''.split('\n')

ranges = defaultdict(lambda: -1)
max_depth = -1

for line in puzzle:
    depth, _range = list(map(int, line.split(': ')))
    ranges[depth] = _range
    max_depth = max(max_depth, depth)

current_positions = [-1 for _ in range(max_depth + 1)]
for depth in ranges.keys():
    current_positions[depth] = 0
current_directions = [1 for _ in range(max_depth + 1)]

position = 0
severity = 0

for depth in range(len(current_positions)):
    if current_positions[position] == 0:
        severity += depth * ranges[position]
    position += 1
    for i in range(len(current_positions)):
        if not i in ranges:
            continue
        if current_directions[i] == 1 and current_positions[i] == ranges[i] - 1:
            current_directions[i] = -1
        elif current_directions[i] == -1 and current_positions[i] == 0:
            current_directions[i] = 1
        current_positions[i] += current_directions[i]

print(severity)
