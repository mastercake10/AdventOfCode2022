lines = list(map(lambda x: x, open("input", "r").readlines()))

def move(multiple: bool):
    num_stacks = len(lines[0])//4

    stacklist = [[] for x in range(num_stacks)]
    for i in range(num_stacks-1, -1, -1):
        for idx,c in enumerate(lines[i]):
            if c.isalpha():
            
                stacklist[idx//4].append(c)

    for line in lines[num_stacks+1:]:
        _, cnt, _, base, _, to = line.strip().split()
        l = []
        for _ in range(int(cnt)):
            l.append(stacklist[int(base)-1].pop())
            
        if multiple:
            l.reverse()
        stacklist[int(to)-1].extend(l)

    return "".join([stack[-1] for stack in stacklist])

print(move(False))
print(move(True))
