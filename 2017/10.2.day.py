

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
    while len(num) < 2:
        num = '0' + num

    return num

def xor(nums):
    return eval(
        str(nums)
            .replace('[', '')
            .replace(']', '')
            .replace(',', ' ^')
    )


def knot_hash(string):
    lengths = list(map(ord, string)) + [17, 31, 73, 47, 23]
    nums = list(range(256))
    position = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            if length != 0:
                reverse_range(nums, position, position + length)
            position += length + skip_size
            position %= len(nums)
            skip_size += 1
    return ''.join(pad_left(hex(knot_hash).replace('0x', '')) for knot_hash in (xor(nums[i * 16:i * 16 +16]) for i in range(16)))

if __name__ == '__main__':
    print(knot_hash('147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'))
