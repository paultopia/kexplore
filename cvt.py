import csv
with open("better-wordlist.csv") as bl:
    lines = bl.readlines()

lines = lines[0:10]

ans = {}
for x in lines:
    m = x.strip().split(",")
    print(m)
