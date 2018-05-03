from collections import defaultdict, deque
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

def is_integer_string(value):
    return re.match(r'^-?\d+$', value)

def is_integer(value):
    return isinstance(value, int)

def wrap_strings(value):
    return "'" + value + "'" if not is_integer_string(value) else value

def to_function_call(command):
    func_name, *args = command.split(' ')
    return 'self.' + func_name + '(' + ', '.join(map(wrap_strings, args)) + ')'

class Program:
    def __init__(self, commands, program_id):
        self.ip = 0
        self.registers = defaultdict(int)
        self.registers['p'] = program_id
        self.commands = commands
        self.queue = deque()
        self.sent_messages_count = 0
        self.other_queue = None
        self.program_id = program_id

    def get_value(self, value_or_register):
        return value_or_register if is_integer(value_or_register) else self.registers[value_or_register]

    def set(self, x, y):
        self.ip += 1
        self.registers[x] = self.get_value(y)

    def add(self, x, y):
        self.ip += 1
        self.registers[x] += self.get_value(y)

    def mul(self, x, y):
        self.ip += 1
        self.registers[x] *= self.get_value(y)

    def mod(self, x, y):
        self.ip += 1
        self.registers[x] %= self.get_value(y)

    def snd(self, x):
        self.ip += 1
        self.sent_messages_count += 1
        self.other_queue.append(self.get_value(x))

    def rcv(self, x):
        if len(self.queue) == 0:
            return
        self.ip += 1
        self.registers[x] = self.queue.popleft()

    def jgz(self, x, y):
        self.ip += self.get_value(y) if self.get_value(x) > 0 else 1

    def tick(self):
        if not self.is_done():
            eval(to_function_call(self.commands[self.ip]))

    def is_locked(self):
        return self.commands[self.ip].startswith('rcv') and len(self.queue) == 0

    def is_done(self):
        return self.ip >= len(self.commands)

    def set_queue(self, queue):
        self.other_queue = queue

    def print_stat(self):
        print('=====================================')
        print('Program ID:', self.program_id)
        print('IP:', self.ip)
        print('Current command:', self.commands[self.ip])
        print('Registers:', self.registers)
        print('Queue:', self.queue)

a = Program(commands, 0)
b = Program(commands, 1)

a.set_queue(b.queue)
b.set_queue(a.queue)

while (not a.is_locked() or not b.is_locked()) and not a.is_done() and not b.is_done():
    a.tick()
    b.tick()

print(b.sent_messages_count)
