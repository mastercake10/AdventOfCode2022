import functools

s = open("input", "r").read()

def cmpr(left: int | list[int, list], right: int | list[int, list]) -> bool | None:
	if type(left) == int and type(right) == int:
		if left == right:
			return None
		return left <= right
	if type(right) != list:
		right = [right]
	if type(left) != list:
		left = [left]
	if not left and not right:
		return False
		
	for l, r in zip(left, right):
		val = cmpr(l, r)
		if val != None:
			return val
	
	return len(left) <= len(right)

packets = list(map(eval, s.strip().replace("\n\n", "\n").split("\n")))

score = 0
for idx, pair in enumerate(list(zip(packets[::2], packets[1::2]))):
	if cmpr(*pair):
		score += idx + 1

print(score)

packets.extend([[2], [6]])
packets.sort(key=functools.cmp_to_key(lambda p1, p2: 1 if cmpr(p1, p2) else -1))

print((packets[::-1].index([2])+1)*(packets[::-1].index([6])+1))
