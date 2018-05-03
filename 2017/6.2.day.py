memory = list(map(int, filter(lambda x: x != '', '5 1   10  0   1   7   13  14  3   12  8   10  7   12  0   6'.split(' '))))

def reallocate_memory_banks(memory):
    max_index, max_value = max(enumerate(memory), key=lambda p: p[1])
    memory[max_index] = 0
    while max_value:
        max_index = (max_index + 1) % len(memory)
        memory[max_index] += 1
        max_value -= 1

    return memory

memory_state_step = {}
steps = 0

while tuple(memory) not in memory_state_step:
    steps += 1
    memory_state_step[tuple(memory)] = steps
    memory = reallocate_memory_banks(memory)
print(steps - memory_state_step[tuple(memory)] + 1)