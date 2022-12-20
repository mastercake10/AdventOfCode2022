import sys
import numpy as np
sys.setrecursionlimit(30**3)

lines = map(lambda x: x.strip(), open("input", "r").readlines())

cubes = set()
for line in lines:
	cubes.add(tuple(map(int, line.split(","))))

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

max = [max([cube[axis] for cube in cubes]) for axis in range(3)]
min = [min([cube[axis] for cube in cubes]) for axis in range(3)]


def creategroup(cube, group=set()):
	x, y, z = cube
	group.add(cube)
		
	for dir in dirs:
		x2 ,y2, z2 = x + dir[0], y + dir[1], z + dir[2]
		cube2 = (x2, y2, z2)
		
		if x2 > max[0]+1 or y2 > max[1]+1 or z2 > max[2]+1 or x2 < min[0]-1 or y2 < min[1]-1 or z2 < min[2]-1:
			continue
		
		if cube2 not in cubes and cube2 not in group:
			creategroup(cube2, group)
			
	return group
	
outer = creategroup((0,0,0))

part1_cnt = 0
part2_cnt = 0
for cube in cubes:
	x,y,z = cube
	for dir in dirs:
		x2,y2,z2 = x+dir[0], y+dir[1],z+dir[2]
		neighbour = (x2, y2, z2)
		
		if neighbour not in cubes:
			part1_cnt += 1
			if neighbour in outer:
				part2_cnt += 1
				
print(part1_cnt)
print(part2_cnt)
