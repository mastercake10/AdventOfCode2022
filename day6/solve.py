s = open("input").readline().strip()

def find_marker(size: int) -> int:
    for i in range(len(s)-size):
        part = s[i:i+size]
        if len(set(part)) == size:
            return i+size
            

print(find_marker(4))
print(find_marker(14))
