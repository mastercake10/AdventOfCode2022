import re

lines = open("input", "r").readlines()

sensors = {}
for line in lines:
	x, y, bx, by = map(int, re.findall(r'\=([\d-]+)[,:\n]', line))
	sensors[(x, y)] = (bx, by)


def dist(a, b):
	dx = abs(b[0] - a[0])
	dy = abs(b[1] - a[1])
	return dx+dy

def merge(intervals):
	merged = [intervals[0]]
	for start, end in intervals[1:]:
		if merged[-1][1] >= start:
			m = (merged[-1][0], max(merged[-1][1], end))
			del merged[-1]
			merged.append(m)
		else:
			merged.append((start, end))
	return merged
		

def calc(mx, sensors, y_, bounds):
	found = []
	for key, val in sensors.items():
		d = val[1]
		x, y = key
		level = d - abs(y_ - y)
		if level < 0:
			continue
		x2 = x-level
		x3 = x+level
		if bounds:
			if x2 > mx:
				continue
			if x2 < 0:
				x2 = 0
			if x3 >= mx:
				x3 = mx
			
		inter = (x2,x3+1)
		
		idx = 0
		if found:
			idx = 0
			for i,f in enumerate(found):
				if f[0] <= inter[0]:
					idx = i+1
			found.insert(idx,inter)
		else:
			found.append(inter)

		found = merge(found)
	return found
mx = 4000000
#mx = 20

sensors = {k: (v, dist(k, v)) for k,v in sensors.items()}
sensors = dict(sorted(sensors.items(), key=lambda x: x[1][1]+x[0][0]))

found = calc(mx, sensors, mx//2, False)
part1 = sum([rng[1] - rng[0] for rng in found])-1

for y_ in range(mx):
	found = calc(mx, sensors, y_, True)
	if y_ % 100000 == 0:
		print(y_)
	if len(found) == 2:
		if found[0][1] - found[1][0] == -1 and found[0][0] == 0 and found[1][1] == mx+1:
			part2 = found[0][1]*mx + y_
			print(y_)
			break

print(part1)
print(part2)
