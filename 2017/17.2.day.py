position = 0
step = 367
zero_position = 0
after_zero_number = None

for i in range(1, 50000000 + 1):
    position = (position + step) % i + 1
    if position == zero_position + 1:
        after_zero_number = i
    if position <= zero_position:
        zero_position += 1

print(after_zero_number)
