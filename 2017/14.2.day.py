from collections import defaultdict
import importlib.util

spec = importlib.util.spec_from_file_location("module.name", "/home/bigbear/AdventOfCode/2017/10.2.day.py")
day10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day10)

spec = importlib.util.spec_from_file_location("module.name", "/home/bigbear/AdventOfCode/2017/12.2.day.py")
day12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day12)

def pad_left(num):
    num = str(num)
    while len(num) < 4:
        num = '0' + num

    return num

graph = defaultdict(list)
all_nodes = set()

for i in range(128):
    row = list(''.join(pad_left(eval('bin(0x%s).replace("0b", "")' % (num))) for num in day10.knot_hash('nbysizxe-' + str(i))))
    for j in range(128):
        if row[j] != '1':
            continue
        all_nodes.add((i, j))
        if (i - 1, j) in all_nodes:
            graph[(i, j)].append((i - 1, j))
            graph[(i - 1, j)].append((i, j))
        if (i, j - 1) in all_nodes:
            graph[(i, j)].append((i, j - 1))
            graph[(i, j - 1)].append((i, j))

# print(graph[(0, 1)])

print(day12.count_groups(graph, all_nodes))
