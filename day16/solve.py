import functools
from itertools import combinations

lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

valves = {}
trans = {}
for idx, line in enumerate(lines):
	from_ = line.split(" ")[1]
	trans[from_] = idx
for line in lines:
	from_ = line.split(" ")[1]
	flow = int(line.split("=")[1].split(";")[0])
	to = frozenset(map(lambda x: trans[x.replace(",", "")], line.split("to ")[1].split()[1:]))
	valves[trans[from_]] = (flow, to)

nonzero = 0
nonzerovalves = []
for valve in valves:
	if valves[valve][0] != 0:
		nonzero += 1
		nonzerovalves.append(valve)

c = 0
vals = {}

@functools.cache
def do(curr, open, tick):
	valve_me = valves[curr]
	flow_me = valve_me[0]
	if tick >= MAX_TICKS:
		return 0
		
	mx = 0
	if not curr in open and flow_me > 0:
		open2 = open.union([curr])
		mx = max(mx, (MAX_TICKS-1-tick)*flow_me + do(curr, open2, tick+1))
			
	for valve2 in valve_me[1]:
		mx = max(mx, do(valve2, open, tick+1))
		
	if len(open) == 7 and MAX_TICKS == 26:
		vals[frozenset(sorted(open))] = mx
	return mx
	
MAX_TICKS = 30
print(do(trans['AA'], frozenset(), 0))

# part 2
MAX_TICKS = 26
combs = list(combinations(nonzerovalves, nonzero//2))
z = 0
i = 0

for human in combs[::-1]:
	for ele in combs:

		if any([e in ele for e in human]):
			continue

		bb1 =  frozenset(sorted(ele)) in vals
		bb2 =  frozenset(sorted(human)) in vals

		he = do(trans["AA"], frozenset(sorted(ele)), 0)
		hv = do(trans["AA"], frozenset(sorted(human)), 0)

		zz = hv + he
		if zz > z:
			#print(bb1, bb2)
			if bb1 and bb2:
				print(z)
				exit()
			z = zz
			#print(z)
