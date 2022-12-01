lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

total = 0
l = []
for line in lines:
    if line:
        total += int(line)
    else:
        l.append(total)
        total = 0
        
s = list(sorted(l))
print(max(s))
print(sum(s[-3:]))

        
