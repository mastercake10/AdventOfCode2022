rounds = list(map(lambda x: x.strip(), open("input", "r").readlines()))

enc = {"X": "A", "Y": "B", "Z": "C"}
shape_vals = {"A": 1, "B": 2, "C": 3}

strategy_win = {"A": "C", "B": "A", "C": "B"}
strategy_lose = {"C": "A", "A": "B", "B": "C"}

value = 0
for round in rounds:
    opp, me = round.split()
    # decrypt to match opponents symbols
    me = enc[me]
   
    value += shape_vals[me]
    if me == opp:
        # draw
        value += 3
    elif me == "A" and opp == "C" or me == "B" and opp == "A" or me == "C" and opp == "B":
        # win
        value += 6
        
print(value)

value = 0
for round in rounds:
    opp, me = round.split() 
    me = enc[me]
   
    if me == "B":
        # draw
        me = opp
        value += 3
    elif me == "A":
        # lose
        me = strategy_win[opp]
    else:
        # win
        me = strategy_lose[opp]
        value += 6
    value += shape_vals[me]

print(value)
