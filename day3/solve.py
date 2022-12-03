lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

translate = lambda y: ord(y)-38 if y.isupper() else ord(y)-96

lines = [list(map(translate, line)) for line in lines]

intersections = []
for line in lines:
    mid = len(line)//2
    compartments = set(line[mid:]), set(line[:mid])
    intersection = compartments[0].intersection(compartments[1])
    intersections.extend(intersection)

print(sum(intersections))

common_groups = list()
for i in range(0, len(lines), 3):
    common = set(lines[i])
    common = common.intersection(lines[i+1])
    common = common.intersection(lines[i+2])
    
    common_groups.append(*common)

print(sum(common_groups))   
