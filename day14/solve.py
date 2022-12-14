import numpy as np

lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))
paths = [list(map(lambda x: tuple(map(int, x.split(","))), path)) for path
					in [line.split(" -> ") for line in lines]]
					
y_max = max([max(map(lambda x: x[1], path)) for path in paths]) + 2					

grid = np.zeros((y_max*10, y_max*2), dtype=np.uint8)

for path in paths:
	for idx in range(len(path)-1):
		x1, y1 = path[idx]
		x2, y2 = path[idx+1]

		if x1 > x2:
			x1, x2 = x2, x1
		if y1 > y2:
			y1, y2 = y2, y1
			
		grid[x1:x2+1, y1:y2+1] = 1

units, part1 = 0, 0
sand_x, sand_y = 500, 0
while not grid[sand_x, sand_y]:
	if sand_y+1 == y_max and part1 == 0:
		part1 = units
	
	for x, y in [(sand_x, sand_y+1),(sand_x-1,sand_y+1),(sand_x+1, sand_y+1)]:
		if not grid[x, y] and sand_y+1 != y_max:
			sand_x, sand_y = x, y
			break
	if sand_x == x and sand_y == y:
		continue

	grid[sand_x, sand_y] = 1	
	units += 1
	sand_x, sand_y = 500, 0
	
print(part1)
print(units)
