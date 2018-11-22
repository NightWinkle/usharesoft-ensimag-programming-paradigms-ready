#!/usr/bin/env python3
import random as rd
import json

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def sort_by(data, var):
    data = data.copy()
    quicksort(data, var)
    return data

def filter_none(data, var):
    filtered_data = []
    for beer in data:
        if not beer[var] is None:
            filtered_data.append(beer)
    return filtered_data

def quicksort(data, var):
    low = 0
    up = len(data) - 1
    q = [(low, up)]
    while(q):
        low, up = q.pop()
        if low < up:
            pivot = choose_pivot(data, low, up)
            pivot = divide(data, low, up, pivot, var)
            q.append((low, pivot-1))
            q.append((pivot+1, up))

def divide(data, low, up, pivot, var):
    data[up], data[pivot] = data[pivot], data[up]
    j = low
    for i in range(low, up):
        if data[i][var] <= data[up][var]:
            data[i], data[j] = data[j], data[i]
            j = j+1
    data[up], data[j] = data[j], data[up]
    return j 

def choose_pivot(data, low, up):
    return rd.randint(low, up)

def main():
    data = load_json('beer_list.json')
    data = filter_none(data, "Gout")
    data = sort_by(data, "Gout")
    for e in data:
        if e["Gout"] == data[-1]["Gout"]:
            print(e["Nom"])

if __name__ == "__main__":
    main()
