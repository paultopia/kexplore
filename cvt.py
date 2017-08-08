import csv
with open("norvig-list.txt") as nl:
    lines = nl.readlines()

lines = lines[0:10]

ans = {}
for x in lines:
    m = x.strip().split("\t")
    ans.update({m[0]: int(m[1])})
print(ans)
