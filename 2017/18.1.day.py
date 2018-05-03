from collections import defaultdict
import re

commands = '''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 680
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''.split('\n')

ip = 0
registers = defaultdict(int)
last_sound_frequence = -1
is_not_recovered = True

def is_integer_string(value):
    return re.match(r'^-?\d+$', value)

def is_integer(value):
    return isinstance(value, int)

def wrap_strings(value):
    return "'" + value + "'" if not is_integer_string(value) else value

def to_function_call(command):
    func_name, *args = command.split(' ')
    return func_name + '(' + ', '.join(map(wrap_strings, args)) + ')'

def snd(x):
    global registers
    global last_sound_frequence
    global ip
    ip += 1
    last_sound_frequence = registers[x]

def set(x, y):
    global registers
    global ip
    ip += 1
    if is_integer(y):
        registers[x] = y
    else:
        registers[x] = registers[y]

def add(x, y):
    global registers
    global ip
    ip += 1
    if is_integer(y):
        registers[x] += y
    else:
        registers[x] += registers[y]

def mul(x, y):
    global registers
    global ip
    ip += 1

    if is_integer(y):
        registers[x] *= y
    else:
        registers[x] *= registers[y]

def mod(x, y):
    global registers
    global ip
    ip += 1
    if is_integer(y):
        registers[x] %= y
    else:
        registers[x] %= registers[y]

def rcv(x):
    global registers
    global last_sound_frequence
    global ip
    global is_not_recovered
    is_not_recovered = False
    ip += 1
    if registers[x] != 0:
        registers[x] = last_sound_frequence

def jgz(x, y):
    global registers
    global ip
    if registers[x] > 0:
        if is_integer(y):
            ip += y
        else:
            ip += registers[y]
    else:
        ip += 1

while is_not_recovered:
    command = commands[ip]
    eval(to_function_call(command))

print(last_sound_frequence)
