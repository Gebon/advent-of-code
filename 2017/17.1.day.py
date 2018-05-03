position = 0
step = 367
buf = [0]

for i in range(1, 2018):
    position = (position + step) % len(buf) + 1
    buf.insert(position, i)

print(buf)
