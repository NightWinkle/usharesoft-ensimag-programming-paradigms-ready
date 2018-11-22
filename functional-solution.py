#!/usr/bin/env python3

import json
import random as rd

def qsort(x, var):
    if len(x) <= 1:
        return x
    pivot = rd.randint(0, len(x) - 1)
    low_part = [x[i] for i in range(len(x)) if x[i][var] < x[pivot][var]]
    up_part = [x[i] for i in range(len(x)) if x[i][var] >= x[pivot][var] and i != pivot]
    return qsort(low_part, var) + [x[pivot]] + qsort(up_part, var)

if __name__ == "__main__":
    with open("beer_list.json", "r") as f:
        data = json.load(f)
    var = "Tx_Alcool"
    sorted_data = qsort([e for e in data if not e[var] is None], var)
    print("\n".join([str(e["Nom"]) for e in sorted_data if e[var] == sorted_data[-1][var]]))
