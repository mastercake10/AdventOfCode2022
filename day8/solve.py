lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

m = [list(map(int, line)) for line in lines]

def is_visible(ma, x, y):
    row = ma[y]
    val = row[x]
    if not row[x+1:] or max(row[x+1:]) < val:
        return True
    if not row[:x] or max(row[:x]) < val:
        return True
    return False

def calc_score(ma, x, y):
    row = ma[y]
    val = row[x]
    a = b = 0
    # east
    if row[x+1:]:
        for t in row[x+1:]:
            a+=1
            if t >= val:
                break
    # west
    if row[:x]:
        for t in row[:x][::-1]:
            b+=1
            if t >= val:
                break
    return a*b


# transposed forest map for vertical calculations
m_T = list(map(list, zip(*m)))
       
scores = []
visible_cnt = 0
for x in range(len(m)):
   for y in range(len(m)): 
        visible_cnt += 1 if is_visible(m, x, y) or is_visible(m_T, y, x) else 0
        scores.append(calc_score(m, y, x) * calc_score(m_T, x, y))
    
print(visible_cnt)
print(max(scores))
