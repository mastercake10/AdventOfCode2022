from numpy import prod
from copy import deepcopy

s =  open("input", "r").read()

monkeys = []

for idx, monkey in enumerate(s.split("\n\n")):
    monkey = monkey.split("\n")
    
    items = monkey[1].split(": ")[1].split(", ")
    op = monkey[2].split(": ")[1]
    div = monkey[3].split(" ")[-1]
    true = monkey[4].split(" ")[-1]
    false = monkey[5].split(" ")[-1]
        
    monkeys.append({"items": list(map(int, items)), "op": op, "div": int(div), "cond": [int(false), int(true)]})

def calc(monkeys: list, divisor: int, rounds: int, mod: bool = False) -> int:
    item_cnt = [0] * len(monkeys)
    for r in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            
            for _ in range(len(monkey["items"])):
                item_cnt[i] += 1
                
                old = monkey["items"].pop(0)
                
                new = eval(monkey["op"].split("new = ")[1])
                if not mod:
                    new //= divisor
                if mod:
                    new %= divisor
                    
                monk_to = monkey["cond"][not new % monkey["div"]]

                monkeys[monk_to]["items"].append(new)

    return sorted(item_cnt)[-1] * sorted(item_cnt)[-2]

print(calc(deepcopy(monkeys), 3, 20))

divisor = prod([monkey["div"] for monkey in monkeys])
print(calc(monkeys, divisor, 10_000, True))
