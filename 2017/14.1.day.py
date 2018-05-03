import importlib.util
spec = importlib.util.spec_from_file_location("module.name", "/home/bigbear/AdventOfCode/2017/10.2.day.py")
day10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day10)

def pad_left(num):
    num = str(num)
    while len(num) < 4:
        num = '0' + num

    return num

result = ''
for i in range(128):
    result += ''.join(pad_left(eval('bin(0x%s).replace("0b", "")' % (num))) for num in day10.knot_hash('nbysizxe-' + str(i)))

print(result.count('1'))
