
file = open('1.txt', 'r')
lines = file.readlines()
file.close()

total = []
left = []
right = []

for i in range(len(lines)):
    cline = lines[i].split('  ')

    cline1 = cline[0].strip()
    cline2 = cline[1].strip()

    left.append(cline1)
    right.append(cline2)

left.sort()
right.sort()

for i in range(len(left)):
    diff = int(left[i]) - int(right[i])

    if diff < 0:
        diff = -diff

    total.append(diff)

print(sum(total))