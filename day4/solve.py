lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

cnt1 = cnt2 = 0
for line in lines:
    elf1, elf2 = line.split(",")
    elf1_a, elf1_b = list(map(int, elf1.split("-")))
    elf2_a, elf2_b = list(map(int, elf2.split("-")))
    
    if elf2_a >= elf1_a and elf2_b <= elf1_b:
        cnt1 += 1
    elif elf1_a >= elf2_a and elf1_b <= elf2_b:
        cnt1 += 1

    pair1 = set(range(elf1_a, elf1_b+1))
    pair2 = set(range(elf2_a, elf2_b+1))
    if pair1.intersection(pair2):
        cnt2 += 1
    
print(cnt1)
print(cnt2)
