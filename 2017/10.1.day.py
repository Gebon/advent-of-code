nums = list(range(256))
lengths = list(map(int, '147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'.split(',')))

position = 0
skip_size = 0

def get_range(nums, start, end):
    end %= len(nums)

    return nums[start:] + nums[:end] if end <= start else nums[start:end]

def set_range(nums, values, start, end):
    end %= len(nums)

    if end <= start:
        nums[start:] = values[:len(nums) - start]
        nums[:end] = values[len(nums) - start:]
    else:
        nums[start:end] = values
    return nums

def reverse_range(nums, start, end):
    return set_range(nums, list(reversed(get_range(nums, start, end))), start, end)

def pad_left(num):
    num = str(num)
    while len(num) < 3:
        num = ' ' + num

    return num

for length in lengths:
    if length != 0:
        reverse_range(nums, position, position + length)
    position += length + skip_size
    position %= len(nums)
    skip_size += 1

print(nums[0] * nums[1])
