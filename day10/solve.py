lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

x = 1
cycle_cnt = 0
total_sum = 0

crt_lines = ""

def cycle(cycles: int) -> None:
    global cycle_cnt, total_sum, crt_lines
    
    for _ in range(cycles):
        cycle_cnt += 1
        crt_lines += "#" if cycle_cnt%40 in range(x, x+3) else "."

        if cycle_cnt%40 == 0:
            crt_lines += "\n"
            
        if (cycle_cnt+20)%40 == 0:
            total_sum += x*cycle_cnt
            
for line in lines:
    params = line.split()
    instruction = params[0]
    
    if instruction == "addx":
        value = int(params[1])
        cycle(2)
        x += value
    else: # noop
        cycle(1) 
        
print(total_sum)
print(crt_lines)
