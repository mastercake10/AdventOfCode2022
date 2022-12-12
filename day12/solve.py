lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

graph = {}
S = ()
E = ()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        graph[(x,y)] = set()
        if c == "S":
            S = (x, y)
        elif c == "E":
            E = (x,y)
            if lines[y][x+1] == "z":
                graph[(x,y)].add((x+1, y))
            if lines[y][x-1] == "z":
                graph[(x,y)].add((x-1, y))
            continue
        
        c1 = ord(c)
        if x < len(line)-1:
            c2 = ord(lines[y][x+1])
            if c1 - c2 <= 1 or c2 == 67 and c == "a":
                graph[(x,y)].add((x+1,y))
        if x > 0:
            c2 = ord(lines[y][x-1])
            if c1 - c2 <= 1 or c2 == ord("S") and c == "a":
                 graph[(x,y)].add((x-1,y))
        if y < len(lines)-1:
            c2 = ord(lines[y+1][x])
            if c1 - c2 <= 1 or c2 == ord("S") and c == "a":
                 graph[(x,y)].add((x,y+1))
        if y > 0:
            c2 = ord(lines[y-1][x])
            if c1 - c2 <= 1 or c2 == ord("S") and c == "a":
                 graph[(x,y)].add((x,y-1))
                 
def dijkstra(graph, start):
    dists = dict()
    prevs = dict()
    q = set()
    for v in graph:
        dists[v] = 1_000_000
        prevs[v] = None
        q.add(v)
        
    dists[start] = 0
    while q:
        u = min(q, key=dists.get)
        q.remove(u)
        
        for v in graph[u]:
            if v in q:
                alt = dists[u] + 1
                if alt < dists[v]:
                    dists[v] = alt
                    prevs[v] = u
    return dists, prevs


# calculating distances from goal to any other coordinate
dist, prev = dijkstra(graph, E)

print(dist[S])

dists = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "a":
            d = dist[(x,y)]
            if d != 0:
                dists.append(d)
print(min(dists))
