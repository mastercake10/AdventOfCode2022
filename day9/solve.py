lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

def calc(segments: int) -> int:
    
    segs = [[0,0] for i in range(segments+1)]
    vis = set()
    for line in lines:
        line = line.split()

        di = line[0]
        val = int(line[1])
        
        for i in range(val):
            head = segs[0]
            hx,hy = head
            if di == "U":
                hy+=1
            elif di == "D":
                hy-=1
            elif di == "L":
                hx-=1
            elif di == "R":
                hx+=1
            segs[0] = hx, hy

            for i in range(len(segs)-1):
                hx, hy = segs[i]
                tx, ty = segs[i+1]
                d = abs(hx-tx) + abs(hy-ty)
                if abs(hx-tx) > 1 or d > 2:
                    if hx > tx:
                        tx += 1
                    elif hx < tx:
                        tx -=1
                if abs(hy-ty) > 1 or d > 2:
                    if hy > ty:
                        ty += 1
                    elif hy < ty:
                        ty -=1
                
                segs[i+1] = tx, ty

            vis.add((segs[-1][0], segs[-1][1]))
    return len(vis)
    
print(calc(1))
print(calc(9))
