mod = 2147483647

def to_bin(num):
    num = bin(num).replace('0b', '')
    if len(num) < 32:
        num = '0' * (32 - len(num)) + num

    return num

def generator(seed, factor):
    while True:
        seed = (seed * factor) % mod
        yield seed

def generator1(start):
    return generator(start, 16807)

def generator2(start):
    return generator(start, 48271)

matches_count = 0

for i, (num1, num2) in enumerate(zip(generator1(699), generator2(124))):
    if to_bin(num1)[-16:] == to_bin(num2)[-16:]:
        matches_count += 1
    if i > 40_000_000 - 2:
        break

print(matches_count)
