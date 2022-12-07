lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

tree = {}
current_dir = []

for line in lines:
    arr = line.split(" ")
    
    if arr[0] == "$":
        ls_mode = False
        cmd = arr[1]
        
        if cmd == "cd":
            arg = arr[2]
            if arg == "/":
                current_dir = []
            elif arg == "..":
                current_dir = current_dir[:-1]
            else:
                current_dir.append(arg)
    else:
        arg1, arg2 = line.split(" ")
        curr = tree
        for key in current_dir:
            if key not in curr:
                curr[key] = {}
            curr = curr[key]
            
        if arg1 == "dir":
            curr[arg2] = {}
        else:
            curr[arg2] = int(arg1)


def walk_dir(tree: dict, path: str, flat_dirs: dict) -> int:
    total_space = 0
    for key in tree:
        if type(tree[key]) == dict:
            total_space += walk_dir(tree[key], path + "/" + key, flat_dirs)
        else:
            total_space += tree[key]

    flat_dirs[path] = total_space
    return total_space

flat_dirs = {}
walk_dir(tree, "", flat_dirs)

print(sum(a for a in flat_dirs.values() if a <= 100_000))

space_required = -70_000_000 + 30_000_000 + flat_dirs['']

for key in list(sorted(flat_dirs, key=lambda x: flat_dirs[x])):
    if flat_dirs[key] >= space_required:
        print(flat_dirs[key])
        break
